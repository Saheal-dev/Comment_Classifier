# Splitting data into training and testing dataset containing only negative comments
import pandas as pd
from sklearn.model_selection import train_test_split

# Load your dataset
df = pd.read_csv("cleaned_comments.csv")  # Replace with your actual file

# Selecting only 'Negative' comments
negative_comments = df[df["Sentiment"] == -1]

# Splitting into 80% training, 20% testing
train_data, test_data = train_test_split(negative_comments, test_size=0.2, random_state=42)

# Save the datasets
train_data.to_csv("train_data.csv", index=False)
test_data.to_csv("test_data.csv", index=False)

print("Train and test datasets created successfully!")