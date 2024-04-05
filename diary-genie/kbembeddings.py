import json
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

# Load the JSON file
with open('diario/book1.json', 'r') as file:
    data = json.load(file)


# Access the list of items under the "val" key
items = data['val']
    
    
# Extract Document Information and filter for published documents
docs = []
for item in items:
    page_content = f"{item.get('text', '')}"

    # Prepare metadata with documentID
    metadata = {"documentID": item.get('id'), "date": item.get("date")}
    # Create a Document object and append to the docs list
    docs.append(Document(page_content=page_content, metadata=metadata))

# Create Embeddings and Initialize Chroma
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
# Note: Assuming Chroma accepts a list of Document objects directly. If not, adjust accordingly.
vectorstore = Chroma.from_documents(docs, embedding_function, persist_directory="./chroma_db")

# Persist the vector store
vectorstore.persist()
