from typing import List, Optional, Type, Union
import threading
import numpy

from langchain.docstore.document import Document
from langchain.text_splitter import (
    CharacterTextSplitter,
    MarkdownTextSplitter,
    TextSplitter,
)
from langchain.vectorstores import Chroma

SPLITTER_TYPE = Union[
    Type[CharacterTextSplitter], Type[TextSplitter], Type[MarkdownTextSplitter]
]


class DataIndexer:
    __db: Chroma

    def __init__(self, db: Chroma) -> None:
        self.__db = db

    def split_into_chunks(
        self,
        documents: List[Document],
        separator="\n",
        chunk_size: int = None,
        chunk_overlap: int = 0,
        splitter: SPLITTER_TYPE = CharacterTextSplitter,
    ) -> List[Document]:
        """Split documents into chunks.

        Args:
            documents: List of documents to split.
            separator: Separator to use for splitting. Defaults to "\n".
            chunk_size: Size of chunks to split into. Defaults to None.
            chunk_overlap: Overlap between chunks. Defaults to 0.
        """
        text_splitter = splitter(
            separator=separator, chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        return text_splitter.split_documents(documents)

    def add_to_database(
        self,
        documents: List[Document],
        ids: Optional[List[str]] = None,
        num_threads: int = 1,
    ):
        """Add documents to database.

        Args:
            documents: List of documents to add.
            ids: List of ids to use for documents. Defaults to None.
            num_threads: Number of threads to use. Defaults to 1.
        """
        if ids is not None and len(documents) != len(ids):
            raise ValueError(
                "Size mismathch: Ids and Documents list should be of same length."
            )
        num_threads = max(1, num_threads)
        if num_threads > 1:
            threads = []

            def add_doc(*args):
                docs = args[0]
                doc_ids = (
                    args[1]
                    if len(args) > 1 and args[1] != None and len(args[1]) > 0
                    else None
                )
                self.__db.add_documents(docs, ids=doc_ids)

            doc_arrays = numpy.array_split(documents, num_threads)
            ids_arrays = (
                numpy.array_split(ids, num_threads) if ids is not None else None
            )

            for index, doc_array in enumerate(doc_arrays):
                ids_array = ids_arrays[index] if ids is not None else None
                t = threading.Thread(
                    target=add_doc,
                    args=(
                        doc_array if isinstance(doc_array, list) else doc_array.tolist(),
                        ids_array if ids_array is None or (ids_array, list) else ids_array.tolist(),
                    ),
                )
                threads.append(t)
                t.start()

            for t in threads:
                t.join()
        else:
            self.__db.add_documents(documents, ids=ids)

        self.__db.persist()
