from flask import Flask, request, jsonify
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import regex as re

app = Flask(__name__)
CORS(app)

# Load the laptop data from the CSV file
laptop_data = pd.read_excel("C:/Users/BAGAS/Downloads/laptop.xlsx")

# Drop the 'ID' column
laptop_data.drop(columns=['perangkatid'], inplace=True)

# Fill NaN values with empty strings to avoid split issues
laptop_data.fillna('', inplace=True)

# Define the fields of study
fields_of_study = [
    {'id': 10001, 'field': 'Teknik dan Teknik Informatika', 'processor': ['Core i5', 'Core i7', 'Ryzen 5 2500U'], 'ram': 8, 'storage': 256, 'storage_type': 'SSD', 'screen': None, 'graphic': ['VGA Nvidia', 'ATI Radeon 2GB']},
    {'id': 10002, 'field': 'Arsitektur', 'processor': ['Core i5', 'Core i7', 'Athlon Gold'], 'ram': 4, 'storage': 256, 'storage_type': 'SSD', 'screen': 'Full HD', 'graphic': ['VGA Nvidia GForce', 'ATI Radeon']},
    {'id': 10003, 'field': 'Desain', 'processor': ['Core i5', 'Core i7', 'Athlon Gold'], 'ram': 8, 'storage': 256, 'storage_type': 'SSD', 'screen': 'Layar IPS anti glare berkualitas', 'graphic': ['VGA Nvidia GForce', 'ATI Radeon']},
    {'id': 10004, 'field': 'Ilmu Komunikasi dan Multimedia', 'processor': ['Core i3 2.0 GHz'], 'ram': 4, 'storage': 512, 'storage_type': 'SSD', 'screen': ['Full HD', 'HD'], 'graphic': ['VGA NVIDIA GForce']},
    {'id': 10005, 'field': 'Akuntansi dan Ilmu Ekonomi', 'processor': ['i5 2.6 GHz', 'FX-9800P'], 'ram': 4, 'storage': [256, 1024], 'storage_type': ['HDD', 'SSD'], 'screen': 'Full HD', 'graphic': None},
    {'id': 10006, 'field': 'Teknik Elektro', 'processor': ['Core i3 2.0 GHz'], 'ram': 8, 'storage': 256, 'storage_type': 'SSD', 'screen': 'Layar 1920x1080 piksel 13 inci', 'graphic': None},
    {'id': 10007, 'field': 'Teknik Sipil', 'processor': ['i5 2.6 GHz', 'FX-9800P'], 'ram': 8, 'storage': 256, 'storage_type': 'SSD', 'screen': 'Layar 14 inci', 'graphic': ['VGA Nvidia Gforce', 'AMD Radeon 1GB']},
    {'id': 10008, 'field': 'Bidang Lainnya', 'processor': ['Core i3', 'Core i8', 'Core i9', 'Dual Core', 'Athlon'], 'ram': 4, 'storage': [256, 500], 'storage_type': ['HDD', 'SSD'], 'screen': ['Full HD', 'HD'], 'graphic': None}
]

# Define the number of clusters
n_clusters = len(fields_of_study)

# Function to extract numeric value from a string or return 0 if not possible
def extract_number(s):
    match = re.search(r'\d+', s)
    return int(match.group()) if match else 0

# Extract and prepare the data for clustering
X = np.array([
    [extract_number(processor),  # Processor
     extract_number(ram),  # RAM
     extract_number(storage),  # Storage
     1 if storage_type.strip().upper() == 'SSD' else 0,  # SSD (1) or HDD (0)
     len(screen.split()),  # Screen
     len(graphic.split())  # Graphic
    ] for processor, ram, storage, storage_type, screen, graphic in zip(
        laptop_data['processor_name'], 
        laptop_data['ram'], 
        laptop_data['storage_capacity'], 
        laptop_data['storage_type'], 
        laptop_data['screen'], 
        laptop_data['graphic']
    )
])

# Perform KMeans clustering
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X)

# Get the cluster labels for each laptop
labels = kmeans.labels_

# Define a mapping from cluster labels to fields of study
cluster_field_mapping = {i: field['field'] for i, field in enumerate(fields_of_study)}

# API endpoint to get cluster label for a given laptop ID
@app.route('/predict', methods=['POST'])
def predict():
    laptop_id = request.json['laptop_id']
    laptop_features = X[laptop_id]
    label = kmeans.predict([laptop_features])[0]
    field = cluster_field_mapping[label]
    return jsonify({'laptop_id': laptop_id, 'field_of_study': field})

@app.route('/recommend', methods=['POST'])
def recommend():
    major = request.json['nama_jurusan']
    major_to_cluster = {field['field']: i for i, field in enumerate(fields_of_study)}
    cluster_label = major_to_cluster.get(major)

    if cluster_label is None:
        return jsonify({'error': 'Invalid major'}), 400

    laptop_indices = [i for i, label in enumerate(labels) if label == cluster_label]
    recommended_laptops = laptop_data.iloc[laptop_indices].to_dict(orient='records')

    return jsonify(recommended_laptops)

if __name__ == '__main__':
    app.run(debug=True, port=5500)
