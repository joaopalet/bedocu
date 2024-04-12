import os

from langchain_google_vertexai import VertexAI

model = VertexAI(model_name="gemini-pro")

file_num_limit = 100


def get_project_summary(file_summaries):
    message = (
        "I will give you a dictionary of filepath and summary, for all files in a project."
        "I want you to write me the README.md for the project. Use # notation for headers."
        "Only use information from the files I give you."
        "\nHere are the file paths and summaries: " + str(file_summaries)
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
    for root, _, files in os.walk(directory):
        if ".git" in root:
            continue
        if "chroma_db" in root:
            continue
        for file in files:
            if "README.md" in file:
                continue
            if "DS_Store" in file:
                continue
            if "go.sum" in file:
                continue
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


directory = "../bedocu"

print("Getting file paths")
file_paths = get_all_file_paths(directory)
if len(file_paths) > file_num_limit:
    print("Too many files to process")
    print("Processed:", len(file_paths))
    print("Limit:", file_num_limit)
    exit(1)
if len(file_paths) == 0:
    print("No files to process")
    exit(1)

print("Getting file summaries")
file_summaries = {}
for file_path in file_paths:
    print(
        "Processing file",
        len(file_summaries) + 1,
        "/",
        len(file_paths),
        "(" + file_path + ")",
    )
    file_summary = get_file_summary(file_path)
    file_summaries[file_path] = file_summary

print("Generating project README")
project_summary = get_project_summary(file_summaries)
with open("out.md", "w") as file:
    file.write(project_summary)
