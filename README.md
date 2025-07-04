# AI Soldier X Bot

An autonomous Python bot that generates and posts fictional but emotionally grounded war dispatches. Each tweet reads like a somber, realistic account from a soldier on the front lines—raw, human, and haunting.

Powered by OpenAI’s ChatGPT and the X (formerly Twitter) API via Tweepy.

---

## Example Output

> Airstrikes hit the northern block before dawn. Communications are down. We’ve lost two from our unit. Still holding the line near the bridge. Supplies low. If anyone can reach us—send word.
---

## Features

- Generates dramatic tweets via OpenAI's GPT-3.5
- Military-style prompt engineering for consistent tone
- Posts directly to X via Tweepy
- Auto-trims to 280 characters

---

## Requirements

- Python 3.8+
- OpenAI API key
- X (Twitter) developer account with access tokens

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-soldier-bot.git
cd ai-soldier-bot
```

### 2. Install Dependencies

```bash
pip install openai tweepy python-dotenv
```

### 3. Create a `.env` File

Create a `.env` file in the root directory and add your API credentials:

```
OPENAI_API_KEY=your_openai_api_key
X_CONSUMER_KEY=your_x_consumer_key
X_CONSUMER_SECRET=your_x_consumer_secret
X_ACCESS_TOKEN=your_x_access_token
X_ACCESS_TOKEN_SECRET=your_x_access_token_secret
```

---

## Run the Bot

```bash
python soldier_bot.py
```

This will generate a tweet using ChatGPT and post it immediately to your X account.

---

## Optional: Automate Posting

To automate posts on a schedule, you can use:

- `cron` (Linux/macOS)
- Task Scheduler (Windows)
- GitHub Actions or other CI/CD tools
- `while True:` loop with `time.sleep()` (not recommended for production)

---

## File Structure

```
ai-soldier-bot/
├── soldier_bot.py     # Main script
├── .env               # API keys (DO NOT COMMIT)
└── README.md          # You're reading it
```

---

## Disclaimers

- All tweets are fictional and generated for creative/entertainment purposes.
- Do not use this bot to impersonate real individuals or post misleading content.

---

## License

MIT — free to fork, modify, and deploy.

---

Made for fun by Soldiers AI.
