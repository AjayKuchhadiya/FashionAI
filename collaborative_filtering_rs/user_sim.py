# 12 items needed?

# Input -> userId, productsPurchased

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

from sklearn.decomposition import TruncatedSVD

def similar_user(userID, user_articles, positive_transactions_parquet, n_components=12):
    try:
        # Read positive_transactions_parquet
        positive_transactions_df = pd.read_parquet(positive_transactions_parquet)
        
        # Concatenate user_articles with userID and convert to DataFrame
        user_data = pd.DataFrame([user_articles], columns=['article_1', 'article_2', 'article_3', 'article_4', 'article_5', 'article_6', 'article_7', 'article_8', 'article_9', 'article_10', 'article_11', 'article_12'])
        user_data['customer_id'] = userID
        
        # Append user_data to positive_transactions_df
        modified_df = pd.concat([positive_transactions_df, user_data], ignore_index=True)
        
        # Generate a user-item interaction matrix (sparse matrix)
        user_item_matrix = modified_df.drop(columns=['customer_id']).apply(pd.to_numeric, errors='coerce').fillna(0)
        
        # Perform dimensionality reduction using Truncated SVD
        svd = TruncatedSVD(n_components=n_components)
        user_item_matrix_reduced = svd.fit_transform(user_item_matrix)
        
        # Compute similarity scores between the target user and all other users
        similarity_scores = cosine_similarity(user_item_matrix_reduced, user_item_matrix_reduced[-1].reshape(1, -1))
        
        # Get indices of top 3 most similar users (excluding the user itself)
        similar_user_indices = similarity_scores.argsort(axis=0)[-4:-1][::-1].flatten()
        
        # Retrieve customer IDs of top 3 most similar users
        similar_users = positive_transactions_df.iloc[similar_user_indices].index.tolist()
        
        return similar_users
    except Exception as e:
        print(f'Error: {e}')
        return []

# Example usage:
userID = '00000dbacae5abe5e23885899a1fa44253a17956c6d1c3d25f88aa139fdfc657'
user_articles = ['0924243001', '0781758057', '0309864012', '0918522001', '0863646004', '0924243002', '', '', '', '', '', '']
positive_transactions_parquet = 'positive_transactions.parquet'

# Call the function
similar_users = similar_user(userID, user_articles, positive_transactions_parquet)

print(f"\n\nTop 3 most similar users for customer {userID} based on their interactions:")
print(similar_users)



# 0924243001 0781758057 0751471001 0309864012 0918522001 0863646004 0924243002 0872537006 0448509014 0562245001 0915529003 0842976005



# 00000dbacae5abe5e23885899a1fa44253a17956c6d1c3d25f88aa139fdfc657,0924243001 0781758057 0751471001 0309864012 0918522001 0863646004 0924243002 0872537006 0448509014 0562245001 0915529003 0842976005



