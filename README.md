# Supabase DB Size Checker

## Index
- [Supabase DB Size Checker](#supabase-db-size-checker)
    - [Index](#index)
    - [Compatibility](#compatibility)
    - [What is it?](#what-is-it)
    - [Project structure](#project-structure)
    - [Compatibility](#compatibility)
- [Setup](#setup)
    - [Clone the repository](#1-clone-the-repository)
    - [Install dependencies](#2-install-dependencies)
    - [Environment variables](#3-environment-variables)
    - [Sql script](#4-sql-script)
    - [Run the monitor](#5-run-the-monitor)
- [Notes](#note)
- [Security Best Practices](#security-best-practices)

## Compatibility
|                |                                                                                                            |
| -------------- | ----------------------------------------------------------------------------------------------------------:|
| Language       | [Python 3.12](https://www.python.org/ "Python's Homepage")                                                  |
| External Packages   | [Supabase 2.6.0](https://github.com/supabase-community/supabase-py "Supabase client for Python")  |
|                | [Requests 2.32.3](https://requests.readthedocs.io "Python HTTP for Humans")         |
|                | [Python Dotenv 1.0.1](https://github.com/theskumar/python-dotenv "Read key-value pairs from a .env file and set them as environment variables")         |

## What is it?
This project monitors the size of a Supabase database and sends notifications to a Discord webhook when the size changes.
That's useful since Supabase has a limit of only 500MB on the free tier.

## Project structure
```
supabase_db_monitor/
├── config/
│ ├── init.py
│ └── settings.py
├── modules/
│ ├── init.py
│ ├── discord.py
│ ├── supabase.py
│ ├── monitor.py
│ └── pickle_utils.py
├── logs/
│ └── monitor_log.txt
├── data/
│ └── previous_size.pkl
├── sql/
│ └── create_get_database_size_function.sql
├── main.py
├── requirements.txt
└── README.md
```


# Setup

## 1. **Clone the repository:**

``` 
git clone [<repository-url>](https://github.com/thomasdoconski/supabase_db_monitor)
cd supabase_db_monitor
```

## 2. **Install dependencies:**

Install the project's dependencies:
```
pip3 install -r requirements.txt
```

## 3. **Environment Variables:**

Create a `.env` file in the root directory and add the following:
- `SUPABASE_URL`: Your Supabase project URL.
- `SUPABASE_KEY`: Your Supabase API key.
- `DISCORD_WEBHOOK_URL`: Your Discord webhook URL.
- `LANGUAGE`: The language for error messages. Options: `en-us`, `pt-br`. Default is `en-us`.

Example `.env` file:
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
DISCORD_WEBHOOK_URL=your_discord_webhook_url
LANGUAGE=en-us
```

>_Optionally_, you can add the environment variable for custom paths to store LOG and PICKLE data and discord.
The variables for path customization are:
- `LOG_FILE_PATH`: Your log file path. 
- `PREVIOUS_SIZE_FILE`: Your pickle file path to store the previous size.
The variable for discord customization are:
- `DISCORD_WEBHOOK_BOT_CUSTOM_NAME`= The name for your discord bot.
- `DISCORD_WEBHOOK_AVATAR_URL`= The profile picture for discord bot.
Example `.env` file with added optional variables:
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
DISCORD_WEBHOOK_URL=your_discord_webhook_url
DISCORD_WEBHOOK_BOT_CUSTOM_NAME=your_discord_bot_custom_name
DISCORD_WEBHOOK_AVATAR_URL=your_discord_avatar_url
LANGUAGE=en-us
LOG_FILE_PATH=your_full_path_for_logs
PREVIOUS_SIZE_FILE=your_full_path_for_pickle
```

## 4. **SQL Script:**

Ensure the function `get_database_size` is created in your Supabase database. 
The script to create this function is located at `./sql/create_get_database_size_function.sql`.

## 5. **Run the monitor:**

Run the Supabase monitoring:
```
python3 -m main.py
``` 

# Notes

Ensure your Python environment is set up correctly and that you are using the correct version of Python (3.x).

# Security Best Practices

To ensure the security of this project, please follow these best practices:

1. **Do not hardcode sensitive information** like API keys, passwords, and credentials.
2. **Use environment variables** to store sensitive data.
3. **Regularly review and update** the `.gitignore` file to ensure sensitive files are not tracked.
4. **Run security scans** before pushing changes to the repository.
5. **Enable GitHub Advanced Security** features to automatically scan for vulnerabilities and secrets.
