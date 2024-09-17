import os

import dotenv
#from langchain.chat_models import AzureChatOpenAI
from langchain_community.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import HumanMessage, AIMessage

from ChatBot import ChatBot


def main():
    embeddings_model = OpenAIEmbeddings(
        deployment=os.environ["EMBEDDINGS_DEPLOYMENT"], chunk_size=1
    )

    db = Chroma(
        persist_directory=os.environ["PERSIST_DIRECTORY"],
        embedding_function=embeddings_model,
    )

    llm = AzureChatOpenAI(
        deployment_name=os.environ["LLM_DEPLOYMENT"],
    )

    chatBot = ChatBot(llm, db)
    chain = chatBot.create()

    conversation_history = []

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        conversation_history.append(HumanMessage(content = user_input))
        response = chain.run(
                question=user_input, chat_history=conversation_history
            )
        print(f"Bot: {response}")
        conversation_history.append(AIMessage(content = response))

if __name__ == "__main__":
    dotenv.load_dotenv()
    main()
