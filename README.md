# RECOMMENDATION-SYSTEM
*COMPANY*: CODETECH IT SOLUTIONS

*NAME*:Gaurav Baburao Gaikwad

*INTER ID*:CODHC18

*DOMAIN*: MACHINE LEARNING

*DURATION*:4 WEEKS

*MENTOR*:NEELA SANTHOSH KUMAR

#A recommendation system is an essential tool in modern data-driven applications, used extensively in e-commerce, streaming platforms, and personalized content delivery. This script implements a recommendation system using Singular Value Decomposition (SVD) on the MovieLens 100K dataset. The goal is to predict user preferences and recommend items based on past interactions.

Dataset Overview
The MovieLens 100K dataset is a widely used benchmark in recommendation system research. It consists of 100,000 user ratings for various movies, with ratings ranging from 1 to 5. The dataset contains three primary components:

User IDs – Unique identifiers for users.
Item IDs (Movies) – Unique identifiers for movies.
Ratings – The ratings provided by users for specific movies.
Preprocessing the Data
The script starts by loading the MovieLens dataset using Pandas. Since the dataset includes timestamps, they are removed to focus only on the user, item, and rating columns. The data is then transformed into a format compatible with the Surprise library, which is specifically designed for building and evaluating recommendation systems.

Model Selection and Training
The recommendation model employs Singular Value Decomposition (SVD), a matrix factorization technique widely used in collaborative filtering. SVD decomposes the user-item interaction matrix into three smaller matrices, capturing latent relationships between users and items. This approach helps in predicting ratings for items that users have not interacted with, enabling recommendations.

The dataset is split into training and testing sets using an 80-20 ratio. The SVD model is trained on the training set, learning underlying patterns in user preferences. Once trained, the model generates predictions for the test set.

Making Predictions
For each user-item pair in the test set, the model estimates a predicted rating. These predictions allow us to understand how closely the model's recommendations align with actual user preferences. The predictions are stored in a Pandas DataFrame and displayed for review.

Evaluation Metrics
To assess the accuracy of the recommendation system, the script computes two key evaluation metrics:

Root Mean Squared Error (RMSE) – Measures the average squared differences between predicted and actual ratings. A lower RMSE indicates better prediction accuracy.
Mean Absolute Error (MAE) – Calculates the average absolute differences between predicted and actual ratings. Like RMSE, a lower MAE signifies improved model performance.
Both RMSE and MAE provide insights into how well the model generalizes to unseen data, helping to fine-tune and optimize future recommendation systems.

Conclusion
This recommendation system demonstrates the fundamental workflow of building a collaborative filtering model using SVD. By leveraging matrix factorization, the model effectively predicts user preferences, which can be extended to real-world applications such as personalized movie recommendations on platforms like Netflix. Further improvements, such as incorporating additional metadata (e.g., genres, user demographics) or hybrid models combining collaborative and content-based filtering, could enhance recommendation accuracy.#
