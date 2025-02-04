# from googleapiclient.discovery import build
# import nltk
# nltk.download('punkt_tab')

# import re
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

# Your API key
# api_key = "AIzaSyBVztYxG-ftSEN6uhSjVykjKgCNKpqSoXA"

# Initialize the YouTube API client
# youtube = build('youtube', 'v3', developerKey=api_key)

# Function to fetch comments for a video
# def get_comments(video_id):
#     comments = []
#     try:
#         # API request to get comment threads
#         request = youtube.commentThreads().list(
#             part="snippet",
#             videoId=video_id,
#             maxResults=100  # Maximum comments per request (up to 100)
#         )
#         response = request.execute()
        
#         # Extract comments
#         for item in response['items']:
#             comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
#             comments.append(comment)
            
#     except Exception as e:
#         print(f"An error occurred: {e}")
    
#     return comments

# Example: Fetch comments for a video
# video_id = "RiEpSd4j0vE"  # Replace with the ID of the YouTube video
# comments = get_comments(video_id)
# print(comments)


# data preprocessing
# import re
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

# def preprocess_text(text):
#     text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)  # Remove links
#     text = re.sub(r'[^A-Za-z\s]', '', text)  # Remove special characters
#     text = text.lower()
#     tokens = word_tokenize(text)
#     stop_words = set(stopwords.words('english'))
#     filtered_tokens = [word for word in tokens if word not in stop_words]
#     return ' '.join(filtered_tokens)

# processed_comments = [preprocess_text(comment) for comment in comments]
# print(processed_comments)

# sentiment analysis--------->
# from textblob import TextBlob

# def get_sentiment(comment):
#     analysis = TextBlob(comment)
#     if analysis.sentiment.polarity > 0:
#         return "Positive"
#     elif analysis.sentiment.polarity < 0:
#         return "Negative"
#     else:
#         return "Neutral"

# sentiments = [get_sentiment(comment) for comment in processed_comments]
# print(sentiments)


# creating suggestions--base on sentiment analysis---->>>
# from collections import Counter

# negative_comments = [comment for comment, sentiment in zip(processed_comments, sentiments) if sentiment == "Negative"]
# keywords = Counter(" ".join(negative_comments).split()).most_common(5)
# print("Top keywords in negative comments:", keywords)
