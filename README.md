# OfCourse

Need somebody to help watch courses for you? Of course!

A handy bot to help you with all your course registration worries. Built for UIUC's course registration system (Banner / Student Self-Service).

Notifications are sent through Mac's Notification Center and Slack. Currently, the bot only watches courses for you instead of auto-registering for them, but future updates can fix this.

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

## Course and term configuration

To set courses to watch, edit `COURSES_TO_WATCH` variable in `src/constants/courses_to_check.py`.

To set term (e.g. Fall 2025, Spring 2026):

1. Go to the course registration page. There should be a dropdown where you can select what term you want.
2. Choose the term you want.
3. Right-click and inspect the page. Tab to Network > Fetch/XHR.
4. Click on the most recent `saveTerm?mode=registration&term=<YOUR_TERM_CODE>&uniqueSessionId=<..>` request.
5. Go to the Payload tab to view parameters more easily.
6. You should see the parameter `term`, which will be your term code! The code should be 6-digit and in the format `120xxx` (at least that has been the trend for 2004-2025).
7. Save this somewhere. You will add it later in your `.env` file as `TERM_CODE`.

<img width="3450" height="638" alt="image" src="https://github.com/user-attachments/assets/0dc16cd8-4a7f-443a-9a0a-e676ebc3fa1d" />

Additional notes on term code:
- This advice might be outdated depending on how it's implemented later, so if you still can't find it look through all the requests to find the most recent 6-digit code.
- There are other ways of finding the code, but this should be an easy way to do so.

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
TERM_CODE=120258 # This is the code for Fall 2025, input the code for your desired term
CHECK_INTERVAL_SECONDS=30
```

Run bot:

```bash
python src/watch.py
``
