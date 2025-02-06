import pandas as pd
import numpy as np
from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate, train_test_split
from surprise.accuracy import rmse, mae

# Load sample dataset (MovieLens 100K as an example)
data = pd.read_csv("https://files.grouplens.org/datasets/movielens/ml-100k/u.data", sep="\t", names=["user_id", "item_id", "rating", "timestamp"])
data = data.drop(columns=["timestamp"])

# Define the Reader object
reader = Reader(rating_scale=(1, 5))

# Load the dataset into Surprise
surprise_data = Dataset.load_from_df(data[['user_id', 'item_id', 'rating']], reader)

# Train-test split
trainset, testset = train_test_split(surprise_data, test_size=0.2)

# Train an SVD model
model = SVD()
model.fit(trainset)

# Make predictions
predictions = model.test(testset)

# Evaluate the model
rmse_score = rmse(predictions)
mae_score = mae(predictions)

# Display sample predictions
predictions_df = pd.DataFrame([(pred.uid, pred.iid, pred.r_ui, pred.est) for pred in predictions], columns=['User', 'Item', 'Actual Rating', 'Predicted Rating'])
print(predictions_df.head())

# Display evaluation results
print(f"RMSE: {rmse_score}")
print(f"MAE: {mae_score}")
