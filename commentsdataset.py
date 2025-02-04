import pandas as pd
import re  # remove special characters , urls 

import nltk
from nltk.tokenize import word_tokenize  #tokenization
from nltk.corpus import stopwords  # remove stopwords

from nltk.stem import WordNetLemmatizer  # lemmatization ( convert word to base form e.g. (running-> run))
 
#  Data set creating ------->>>>>>.
# Load the dataset (replace 'your_dataset.csv' with your actual dataset file path)
df = pd.read_csv('Datasets/YoutubeCommentsDataSet.csv',encoding='ISO-8859-1')

# Check the first few rows to verify column names
print(df.head())
print(f"Rows: {df.shape[0]}") 


# print("Negative comments have been saved to 'negative_comments.csv'.")

# data preprpocessing ----->>>>>>

# 1) Remove duplicate data

# Drop duplicates
df = df.drop_duplicates(subset=['Comment'])

# Drop missing values
df = df.dropna()

# Reset index
df = df.reset_index(drop=True)
print(f"Rows: {df.shape[0]}") 


# 2) Convert to lowercase 
df['Comment'] = df['Comment'].str.lower()


# 3) Remove URL's special characters & words
def clean_text(text):
    text = re.sub(r"http\S+|www\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters & numbers
    return text

df['Comment'] = df['Comment'].apply(clean_text)


# 4)Tokenization (break the comments into individual words )
nltk.download('punkt')

df['Comment'] = df['Comment'].apply(word_tokenize)

# 5) remove stopwords 
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

df['Comment'] = df['Comment'].apply(lambda x: [word for word in x if word not in stop_words])


# 6) lemmatization ( convert word to base form e.g. (running-> run))
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

df['Comment'] = df['Comment'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])

# 7) Convert Tokenized Words Back to Sentences
df['Comment'] = df['Comment'].apply(lambda x: " ".join(x))


# 8) Encode Sentiments
sentiment_mapping = {'positive': 1, 'neutral': 0, 'negative': -1}
df['Sentiment'] = df['Sentiment'].map(sentiment_mapping)
print(df.head())


#  save clean / preprocessed data to new dataset/csv file
df.to_csv("cleaned_comments.csv", index=False)
print("Preprocessing complete! Cleaned data saved to 'cleaned_comments.csv'")


