from langchain_google_vertexai import VertexAI

model = VertexAI(model_name="gemini-pro")

file_num_limit = 50
file_lines_limit = 200

processed_files_count = 0


def getFileSummary(filepath):
    f = open(filepath, "r")
    contents = f.read()
    message = (
        "I will give you the contents of a file and I want you to return me the summary of its content in simple plain text. The file content is: "
        + contents
    )
    res = model.invoke(message)
    return res


res = getFileSummary("./example-project/website-builder/app/__init__.py")
print(res)
