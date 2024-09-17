import glob
from pathlib import Path
from typing import List, Type, Union

from langchain.docstore.document import Document
from langchain.document_loaders import (
    BSHTMLLoader,
    DirectoryLoader,
    TextLoader,
    UnstructuredFileLoader,
    UnstructuredMarkdownLoader,
)

FILE_LOADER_TYPE = Union[
    Type[UnstructuredFileLoader],
    Type[TextLoader],
    Type[BSHTMLLoader],
    Type[UnstructuredMarkdownLoader],
]


class DataLoader:
    def __init__(
        self,
        path: str = None,
        glob: str = "**/[!.]*",
        file_list: list[str] = None,
        loader_cls: FILE_LOADER_TYPE = UnstructuredFileLoader,
    ):
        """Initialize with a path to directory and how to glob over it.

        Args:
            path: Path to directory.
            glob: Glob pattern to use to find files. Defaults to "**/[!.]*"
                (all files except hidden).
            loader_cls: Loader class to use for loading files.
                Defaults to UnstructuredFileLoader.
        """
        self.path = path
        self.glob = glob
        self.loader_cls = loader_cls
        self.file_list = file_list

    def load_file(self, item: Path, docs: List[Document]) -> None:
        """Load a file.

        Args:
            item: File path.
            docs: List of documents to append to.
            pbar: Progress bar. Defaults to None.

        """
        if item.is_file():
            try:
                print(f"Processing file: {str(item)}")
                sub_docs = self.loader_cls(str(item), encoding="utf-8").load()
                docs.extend(sub_docs)
            except Exception as e:
                print(f"Error loading file {str(item)}: {e}")

    def load(self) -> List[Document]:
        """If path is not none, load all the globbed files in that path. If path is none, load the file list."""
        docs = []
        if self.path is not None:
            loader = DirectoryLoader(
                self.path,
                glob=self.glob,
                loader_cls=self.loader_cls,
                loader_kwargs={"encoding": "utf-8"},
            )
            docs = loader.load()
        else:
            for patterns in self.file_list:
                for file in glob.glob(patterns, recursive=True):
                    item = Path(file)
                    self.load_file(item, docs)
        return docs
