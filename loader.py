import os
from urllib.parse import unquote

import dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

from DataIndexer import DataIndexer
from DataLoader import DataLoader, TextLoader


def load_data():
    loader = DataLoader(file_list=["**/*.md"], loader_cls=TextLoader)
    documents = loader.load()
    if documents is None or len(documents) == 0:
        raise ValueError("No documents found.")

    embeddings_model = OpenAIEmbeddings(
        deployment=os.environ["EMBEDDINGS_DEPLOYMENT"],
        show_progress_bar=True,
    )

    db = Chroma(
        persist_directory=os.environ["PERSIST_DIRECTORY"],
        embedding_function=embeddings_model,
    )

    data_indexer = DataIndexer(db)
    docs = documents
    docs = data_indexer.split_into_chunks(documents, chunk_size=1024, chunk_overlap=128)
    for doc in docs:
        doc.page_content = unquote(str(doc.metadata)) + "\n" + doc.page_content
    data_indexer.add_to_database(docs, num_threads=4)


if __name__ == "__main__":
    dotenv.load_dotenv()
    load_data()
