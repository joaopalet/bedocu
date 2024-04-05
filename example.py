from langchain_google_vertexai import VertexAI

model = VertexAI(model_name="gemini-pro")

f = open("./example-project/website-builder/app/__init__.py", "r")
contents = f.read()
message = (
    "This is the contents of a file. Based on it, generate a summary of its functionality. File: "
    + contents
)
res = model.invoke(message)

print(res)
