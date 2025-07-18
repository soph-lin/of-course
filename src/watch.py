import time
import requests
import os
from dotenv import load_dotenv
import sys
from constants.courses_to_check import COURSES_TO_WATCH
from util.message import notify_slack, notify_mac

# Load config
load_dotenv()

TERM_CODE = os.getenv("TERM_CODE")
CHECK_INTERVAL_SECONDS = int(os.getenv("CHECK_INTERVAL_SECONDS", 30))
UNIQUE_SESSION_ID = f"watcher{int(time.time())}"

# Helper

def check_course(subject, course_number, section_to_match, term_code):
    url = "https://banner.apps.uillinois.edu/StudentRegistrationSSB/ssb/searchResults/searchResults"
    params = {
        "txt_subject": subject,
        "txt_courseNumber": course_number,
        "txt_term": term_code,
        "startDatepicker": "",
        "endDatepicker": "",
        "uniqueSessionId": UNIQUE_SESSION_ID,
        "pageOffset": 0,
        "pageMaxSize": 10,
        "sortColumn": "subjectDescription",
        "sortDirection": "asc",
    }
    headers = {
        "Accept": "application/json",
        "X-Requested-With": "XMLHttpRequest"
    }

    r = requests.get(url, params=params, headers=headers)
    r.raise_for_status()
    response_data = r.json()

    found = False
    
    data = response_data.get("data")
    if data is None:
        raise RuntimeError(
            f"No course data returned for {subject} {course_number} — "
            "the session may have expired and you need to log in again."
        )

    for section in data:
        sequence_number = section.get("sequenceNumber", "").strip()
        seats = int(section.get("seatsAvailable", 0))
        open_flag = section.get("openSection", False)

        if sequence_number != section_to_match:
            continue

        print(f"[CHECK] {subject} {course_number} {sequence_number}: {seats} seat(s) | Open: {open_flag}")
        
        if seats > 0 and open_flag:
            msg = (
                f"🎉 {subject} {course_number} - Section {sequence_number} has {seats} seat(s) available!"
                f" Check Banner now to register!"
            )
            print(f"🎯 Found open seat: {subject} {course_number} Section {sequence_number} — {seats} seat(s) available")
            notify_slack(msg)
            notify_mac(msg)
            found = True

    return found

# Main

def run():
    print(f"🚀 Watching {len(COURSES_TO_WATCH)} courses for open seats...")
    while True:
        try:
            any_found = False
            for course in COURSES_TO_WATCH:
                subject = course["subject"]
                number = course["number"]
                section = course["section"]
                found = check_course(subject, number, section, TERM_CODE)
                any_found = any_found or found
            if any_found:
                print("✅ At least one seat found. Exiting.")
                break
        except RuntimeError as e:
            print(f"[FATAL ERROR] {e}")
            sys.exit(1)
        except Exception as e:
            print("[ERROR]", e)
        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    run()
