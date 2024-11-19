
# TeleBazi

TeleBazi is a Python-based Telegram bot designed to provide interactive features using the `python-telegram-bot` library. The bot is easily configurable and supports dynamic functionalities with customizable handlers.

## Features
- Command and message handling for Telegram users.
- Secure configuration using environment variables.
- Logging for monitoring and debugging.

## Project Structure
```
.
├── bot.py             # Main bot script
├── modules/           # Additional modules for bot functionality
├── .env               # Environment variables (e.g., Telegram token)
├── bot_logs.log       # Log file for runtime activities
└── .idea/             # IDE-specific settings
```

## Requirements
- Python 3.8+
- Required libraries listed in `requirements.txt`

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/dat3be/telebazi.git
   cd telebazi
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the project root:
   ```env
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```

4. **Run the Bot:**
   ```bash
   python bot.py
   ```

## Logging
Logs are stored in `bot_logs.log` for monitoring bot activities and debugging.

## Contributions
Feel free to fork and submit pull requests to improve the bot!

## License
This project is open-source and available under the [MIT License](LICENSE).
