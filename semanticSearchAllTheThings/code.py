import os
import faiss
import numpy as np
import pickle
import hashlib
from sentence_transformers import SentenceTransformer

def calculate_directory_hash(directory_path):
    hash_md5 = hashlib.md5()
    for subdir, _, files in os.walk(directory_path):
        for file in sorted(files, key=lambda x: x.lower()):  # sorting ensures consistent order
            with open(os.path.join(subdir, file), 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
    return hash_md5.hexdigest()

def load_data_from_directory(directory_path):
    documents = {}
    for file in os.listdir(directory_path):
        if file.endswith(".txt"):
            with open(os.path.join(directory_path, file), 'r', encoding='utf-8') as f:
                documents[file] = f.readlines()
    return documents

def vectorize_data(documents, model):
    all_lines = [line for lines in documents.values() for line in lines]
    embeddings = model.encode(all_lines)
    return all_lines, np.array(embeddings)

def build_faiss_index(embeddings):
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index

def search(query, model, index, all_lines):
    query_embedding = model.encode([query])[0]
    D, I = index.search(np.array([query_embedding]), 1)
    return all_lines[I[0][0]]

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    current_hash = calculate_directory_hash(directory_path)
    embeddings_path = "embeddings.pkl"
    hash_path = "directory_hash.txt"

    model = SentenceTransformer('paraphrase-distilroberta-base-v1')  # Initialize model once

    # Check if the hash of the directory matches the saved hash and if embeddings file exists
    if (os.path.exists(hash_path) and os.path.exists(embeddings_path) and
            open(hash_path, 'r').read() == current_hash):
        with open(embeddings_path, 'rb') as f:
            all_lines, embeddings = pickle.load(f)
    else:
        documents = load_data_from_directory(directory_path)
        all_lines, embeddings = vectorize_data(documents, model)

        # Save embeddings and directory hash
        with open(embeddings_path, 'wb') as f:
            pickle.dump((all_lines, embeddings), f)
        with open(hash_path, 'w') as f:
            f.write(current_hash)

    index = build_faiss_index(embeddings)

    while True:
        query = input("Enter a line of text for similarity search (or 'exit' to stop): ")
        if query == "exit":
            break
        most_similar_line = search(query, model, index, all_lines)
        print(f"Most similar line: {most_similar_line}")
