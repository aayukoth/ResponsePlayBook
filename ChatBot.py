from typing import Any
#from langchain.chat_models import AzureChatOpenAI
from langchain_community.chat_models import AzureChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Chroma
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)


class ChatBot:
    __llm: AzureChatOpenAI
    __db: Chroma
    bot: ConversationalRetrievalChain

    def __init__(self, llm: AzureChatOpenAI, db: Chroma):
        self.__llm = llm
        self.__db = db

    def create(self) -> ConversationalRetrievalChain:
        general_system_template = """Use the following pieces of context to answer the users question. If you cannot find the answer from the pieces of context, just say that you don't know, don't try to make up an answer.

        ----------------
        {context}"""
        general_user_template = "Question:```{question}```"

        messages = [
            SystemMessagePromptTemplate.from_template(general_system_template),
            HumanMessagePromptTemplate.from_template(general_user_template),
        ]
        qa_prompt = ChatPromptTemplate.from_messages(messages)

        self.bot = ConversationalRetrievalChain.from_llm(
            llm=self.__llm,
            max_tokens_limit=16384,
            chain_type="stuff",
            retriever=self.__db.as_retriever(k=10),
            verbose=True,
            combine_docs_chain_kwargs={"prompt": qa_prompt},
        )

        return self.bot

    def run(self, query: Any):
        return self.bot.run(query)
