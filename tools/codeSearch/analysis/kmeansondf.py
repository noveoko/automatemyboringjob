from sklearn.cluster import KMeans
import pandas as pd

# Assuming 'your_dataframe' is your DataFrame containing integers
# Replace 'your_dataframe' with the actual name of your DataFrame
# Also, replace the column names if needed

# Step 1: Import your DataFrame
# your_dataframe = pd.read_csv('your_data.csv')  # Use the appropriate method to load your data

# Step 2: Initialize KMeans model with the number of clusters (6 in your case)
kmeans_model = KMeans(n_clusters=6, random_state=42)

# Step 3: Fit the model to your data
kmeans_model.fit(your_dataframe)

# Step 4: Get cluster labels for each data point
cluster_labels = kmeans_model.labels_

# Step 5: Add the cluster labels to your DataFrame
your_dataframe['Cluster'] = cluster_labels

# Now, your DataFrame has an additional 'Cluster' column with the assigned cluster labels