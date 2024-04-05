**README.md**

**Diary Genie**

**Summary**

Diary Genie is a conversational AI that uses natural language processing (NLP) and machine learning to help users access and analyze their personal diary entries. It features:

- **Document Embeddings:** Diary entries are transformed into vector representations using SentenceTransformer, enabling similarity search for efficient retrieval.
- **Similarity Search:** Users can ask questions about their diary entries, and Diary Genie retrieves and displays the most relevant entries based on semantic similarity.
- **Interactive Interface:** Users can interact with Diary Genie through a command-line interface, asking questions and receiving personalized responses.
- **Document Details:** In addition to displaying relevant entries, Diary Genie also provides document metadata, such as date and time of entry.

**Usage**

1. **Requirements:** Python 3.6 or later, SentenceTransformer, Chroma
2. **Installation:** pip install -r requirements.txt
3. **Usage:** Run `diary-genie.py` and follow the prompts to interact with the model.

**Example**

```
> What was a memorable day in September?
>
> on 15-09-2023, had a delicious meal with friends
```

**Benefits**

- **Improved Memory Recall:** Diary Genie makes it easier for users to recall past experiences by quickly retrieving relevant diary entries.
- **Personalized Insights:** The model analyzes diary entries to identify patterns and provide personalized insights into the user's past.
- **Reflective Tool:** Diary Genie encourages users to reflect on their past experiences and appreciate the good moments in life.

**Note:** The diary entries used in this project are for demonstration purposes only. Please replace them with your own personal diary entries for a more personalized experience.
