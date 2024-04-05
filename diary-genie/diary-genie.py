import os

from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_vertexai import VertexAI

# Create Embeddings and Initialize Chroma
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(
    persist_directory="./chroma_db", embedding_function=embedding_function
)


model = VertexAI(model_name="text-unicorn")


def get_answer(entries, query):
    message = (
        "I will give you context from my previous notes. Based in that, you need to provide an answer (a normal sentence in plain text) to my query."
        "You are free to make assumptions based in the context, but if you do so, ALWAYS warn the user."
        "\nHere is the context: "
        + str(entries)
        + "\nAnd here is the query: "
        + str(query)
    )
    res = model.invoke(message)
    return res


def askFM():
    while 1:
        prompt = input("Enter a question about your diary: ")
        results = vectorstore.similarity_search(prompt)

        context_for_llm = []
        ii = 0
        for i in range(len(results)):
            entry = (
                "{"
                + '"date": "'
                + results[i].metadata["date"]
                + '", "text": "'
                + results[i].page_content
                + '"}'
            )
            ii += 1
            context_for_llm += [entry]
            if i > 4:  # number of top results to feed to the LLM for context
                break

        out = get_answer(context_for_llm, prompt)
        print(out, "\n")


askFM()
