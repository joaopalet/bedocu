import os

from langchain_google_vertexai import VertexAI

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


entries = """
    {
        "date": "01-09-2023",
        "text": "Today was sunny and I ate a beef hamburger"
    },
    {
        "date": "12-10-2023",
        "text": "Today it rained and I broke my leg"
    },
    {
        "date": "23-11-2023",
        "text": "Today it was sunny and I found money on the ground"
    },
    {
        "date": "04-02-2023",
        "text": "Today it rained and I had an accident"
    }
"""
query = input("What do you want to know?\n  -> ")  # "When did I become richer?"
project_summary = get_answer(entries, query)
print("\n" + project_summary)
