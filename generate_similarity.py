import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Step 1: Load your dataset
movies_data = pd.read_csv('movies_data.csv')

# Step 2: Create 'tags' column by combining relevant text features
movies_data['tags'] = (
    movies_data['TITLE'].astype(str) + ' ' +
    movies_data['MAIN_GENRE'].astype(str) + ' ' +
    movies_data['MAIN_PRODUCTION'].astype(str)
)

# Step 3: Replace NaNs if any
movies_data['tags'] = movies_data['tags'].fillna('')

# Step 4: Create TF-IDF matrix from 'tags'
vectorizer = TfidfVectorizer(stop_words='english')
feature_vectors = vectorizer.fit_transform(movies_data['tags'])

# Step 5: Compute cosine similarity
similarity = cosine_similarity(feature_vectors)

# Step 6: Save similarity matrix to a file
pickle.dump(similarity, open('similarity.pkl', 'wb'))

# Optional: Save the updated CSV with tags
movies_data.to_csv('movies_data.csv', index=False)

print("✅ similarity.pkl created successfully.")
