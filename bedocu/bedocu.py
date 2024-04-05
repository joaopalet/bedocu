import os

from langchain_google_vertexai import VertexAI

model = VertexAI(model_name="gemini-pro")

file_num_limit = 40


def get_project_summary(file_summaries):
    message = (
        "I will give you the filepath and summaries of all files in a project."
        "I want you to write me a summary of the whole project. E.g write me a README.md for the project."
        "\nThe files summary: " + str(file_summaries)
    )
    res = model.invoke(message)
    return res


def get_file_summary(file_path):
    f = open(file_path, "r")
    contents = f.read()
    message = (
        "I will give you the contents of a file and I want you to return me the summary of its content in plain text."
        "No paragraphs and no bullet points."
        "\nThe file content is: " + contents
    )
    res = model.invoke(message)
    return res


def get_all_file_paths(directory):
    file_paths = []
    processed_files_count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
            processed_files_count += 1
            # Exit if number of files is bigger than limit
            if processed_files_count > file_num_limit:
                return []
    return file_paths


directory = "./example-projects/website-builder"
file_paths = get_all_file_paths(directory)
file_summaries = {}
for file_path in file_paths:
    file_summary = get_file_summary(file_path)
    file_summaries[file_path] = file_summary

project_summary = get_project_summary(file_summaries)
print(project_summary)
