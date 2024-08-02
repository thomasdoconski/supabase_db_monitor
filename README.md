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
- [Note](#note)

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
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
DISCORD_WEBHOOK_URL=your_discord_webhook_url
```

## 4. **SQL Script:**

Ensure the function `get_database_size` is created in your Supabase database. 
The script to create this function is located at `./sql/create_get_database_size_function.sql`.

## 5. **Run the monitor:**

Run the Supabase monitoring:
```
python3 -m main.py
``` 

## Note

Ensure your Python environment is set up correctly and that you are using the correct version of Python (3.x).
