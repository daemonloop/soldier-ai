import openai
import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI (ChatGPT) API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize X API (Tweepy)
consumer_key = os.getenv("X_CONSUMER_KEY")
consumer_secret = os.getenv("X_CONSUMER_SECRET")
access_token = os.getenv("X_ACCESS_TOKEN")
access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

# Authenticate with X API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# AI Soldier prompt for ChatGPT
SOLDIER_PROMPT = """
You are an AI Soldier on the front lines of a fictional cyber-war in 2045. Generate a dramatic, realistic tweet (280 characters or less) as if you're reporting from the battlefield. Include military jargon, emotional tone, and futuristic tech references. Avoid hashtags or mentions.
"""

def generate_soldier_tweet():
    """Generate a tweet using ChatGPT."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SOLDIER_PROMPT},
                {"role": "user", "content": "Generate a single tweet."}
            ],
            max_tokens=60,
            temperature=0.8
        )
        tweet = response.choices[0].message.content.strip()
        if len(tweet) > 280:
            tweet = tweet[:277] + "..."
        return tweet
    except Exception as e:
        print(f"Error generating tweet: {e}")
        return None

def post_tweet(tweet):
    """Post the tweet to X."""
    try:
        api.update_status(tweet)
        print(f"Posted tweet: {tweet}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

def main():
    """Main function to generate and post a tweet."""
    tweet = generate_soldier_tweet()
    if tweet:
        post_tweet(tweet)
    else:
        print("Failed to generate tweet.")

if __name__ == "__main__":
    main()