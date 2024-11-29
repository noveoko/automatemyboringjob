# Text Similarity Search with FAISS

A simple Python-based utility to perform semantic similarity search on lines of text across multiple files using the FAISS library and sentence embeddings.

## Features

- Load text data from multiple files in a directory.
- Vectorize each line from all files using sentence embeddings.
- Create an efficient search index using FAISS.
- Search for the most similar line given a query.

## Prerequisites

Ensure you have the following libraries installed:

```bash
pip install sentence-transformers faiss-cpu
```

## Usage

1. **Load Data:** 
   
   Place all your `.txt` files containing text data in a directory.

2. **Run the Program:** 

   Execute the Python script and provide the directory path containing the text files when prompted.

   ```bash
   python faiss_similarity_search.py
   ```

3. **Perform Searches:** 

   Input lines of text to find the most similar line from the files. Type `exit` to stop the program.

## How It Works

1. **Sentence Transformers for Vectorization:** The program leverages the `sentence-transformers` library, which provides high-quality sentence embeddings. Specifically, it uses the `paraphrase-distilroberta-base-v1` model.

2. **FAISS Indexing:** FAISS (Facebook AI Similarity Search) is a library for efficient similarity search and clustering of dense vectors. This program utilizes FAISS to index the embeddings of each line of text, enabling fast similarity searches.

3. **Search:** For any given query, the program finds the most semantically similar line of text from the indexed vectors.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements

- [sentence-transformers](https://github.com/UKPLab/sentence-transformers)
- [FAISS](https://github.com/facebookresearch/faiss)

---

I hope this helps you get started with your text similarity search project!
