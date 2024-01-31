from sklearn.cluster import KMeans
import pandas as pd

# Assuming 'your_dataframe' is your DataFrame containing integers
# Replace 'your_dataframe' with the actual name of your DataFrame
# Also, replace the column names if needed

# Step 1: Import your DataFrame
# your_dataframe = pd.read_csv('your_data.csv')  # Use the appropriate method to load your data

# Store the index in a separate variable
index_column = your_dataframe.index

# Drop the index column for clustering
data_for_clustering = your_dataframe.drop(index_column, axis=1)

# Step 2: Initialize KMeans model with the number of clusters (6 in your case)
kmeans_model = KMeans(n_clusters=6, random_state=42)

# Step 3: Fit the model to your data
kmeans_model.fit(data_for_clustering)

# Step 4: Get cluster labels for each data point
cluster_labels = kmeans_model.labels_

# Step 5: Add the cluster labels to your DataFrame
your_dataframe['Cluster'] = cluster_labels

# Restore the index column
your_dataframe.index = index_column

# Now, your DataFrame has an additional 'Cluster' column with the assigned cluster labels