import openai
import tweepy
import os
import random
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

# Prompt for battlefield comms (realistic, grounded)
COMMS_PROMPT = """
You are a soldier reporting from the front lines of a modern war. Write a tweet (280 characters or less) as if it’s being sent over radio or unit comms. Keep the tone raw, emotional, and realistic. Mention location, losses, supplies, morale—anything a real soldier might report.
Avoid hashtags or mentions.
"""

# Prompt for writing home (letter-style)
LETTER_PROMPT = """
You are a soldier writing a short message home during a modern war. Write a single tweet (280 characters or less) like a letter to a loved one. Reflect exhaustion, fear, longing, or quiet hope. Keep it grounded and emotional, as if written in a moment of calm.
Avoid hashtags or mentions.
"""

def generate_soldier_tweet():
    """Randomly generate a comms report or a letter home tweet using ChatGPT."""
    prompt_type = random.choice(["comms", "letter"])
    system_prompt = COMMS_PROMPT if prompt_type == "comms" else LETTER_PROMPT

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": "Generate a single tweet."}
            ],
            max_tokens=80,
            temperature=0.85
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
