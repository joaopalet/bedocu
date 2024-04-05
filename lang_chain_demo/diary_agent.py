from langchain_community.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings




# Create Embeddings and Initialize Chroma
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding_function)






def askFM():
    while 1:
        prompt = input("Enter a question about your diary: ")
        results = vectorstore.similarity_search(prompt)
        
        for i in range(5): # number of top results to feed to the LLM for context
            print(i)
            {}
        
        print(prompt)
        
        
askFM()




# Displaying results
for result in results:
    print(f"Document: {result.page_content[:100]}, Metadata: {result.metadata}")
