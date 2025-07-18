# About

Notifications are sent through Mac's Notification Center and Slack.

Inspired by [https://github.com/riteofthearcane/AutoRegister](https://github.com/riteofthearcane/AutoRegister).

# Setting up

## Install `terminal-notifier`

The repository can be found at [https://github.com/julienXX/terminal-notifier](https://github.com/julienXX/terminal-notifier).

Install:

```bash
brew install terminal-notifier
```

Try running an example command to make sure it works:

```bash
echo 'Piped Message Data!' | terminal-notifier -sound default
```

Make sure to turn on Notifications for `terminal-notifier` in Settings App.

$ echo 'Piped Message Data!' | terminal-notifier -sound default

## Create Slack webhook

[Create a Slack workspace](https://slack.com/create) for receiving the notifications if you don't already have one in mind. Otherwise, sign in to that workspace.

Create a new channel in the workspace, e.g. `#course-alerts`.

Create a new application on [https://api.slack.com/apps](https://api.slack.com/apps):

1. Click “Create New App”
2. From scratch → Name: CourseAlertBot → Select your workspace
3. Go to the app dashboard.
4. Click “Incoming Webhooks”
5. Enable “Activate Incoming Webhooks”
6. Click “Add New Webhook to Workspace”
7. Choose your channel (e.g. `#course-alerts`)
8. You can now copy the webhook URL (should look something like `https://hooks.slack.com/services/T0000/...`). Keep this tab open since you will be copying this into your `.env` file later.

## Find term

## Install code

Create and activate virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

Download dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file and add environment variables:

```bash
# API
SLACK_WEBHOOK_URL=<YOUR_WEBHOOK_URL>

# Global settings
TERM_CODE=120258 # Fall 2025
CHECK_INTERVAL_SECONDS=30
```

Run bot:

```bash
python src/watch.py
```
