from langchain_google_vertexai import VertexAI

model = VertexAI(model_name="gemini-pro")

file_num_limit = 50
file_lines_limit = 200

processed_files_count = 0


def getFileSummary(filepath):
    f = open(filepath, "r")
    contents = f.read()
    message = (
        "This is the contents of a file. Based on it, generate a summary of its functionality. File: "
        + contents
    )
    res = model.invoke(message)
    return res


res = "./example-project/website-builder/app/__init__.py"
print(res)
