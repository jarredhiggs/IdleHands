# TODO - Idle Hands

**"Discipline isn't learned. It's enforced."**

---

Next:
    - Create basic framework for interaction with LLM (mocked)
    - 

## Core Activity Monitor

Track app usage, idle time, user input, and log it all.

- System-wide active window tracker
    - Windows: `pywin32` / `ctypes`
- Idle detection via keyboard/mouse
    - Libraries: `pynput`, `pyxhook`
- Foreground app name + process ID logging
- Input volume tracking (keystrokes/mouse clicks per minute)
- User journal for justification / excuses
- Store all data to local database (`sqlite` or JSON)

---

## ChatGPT Integration

The imp behind the curtain. Drives feedback, insults, and guidance.

- Integrate ChatPT API
- Send summaries of activity logs for response
- Contextual insult/advice engine powered by GPT


## Rule Engine + Thresholds

This is where the daemon judges you.

- Configurable idle time thresholds
- Forbidden app list

* Set up local activity logger module
* Write app usage tracking backend
* Build insult feedback system (TTS or audio clips)
* UI overlay mockup
* Configuration interface for thresholds and schedules
* Webhook system for optional shock hardware
* Logging system with timeline visualization
* Implement sarcasm detection (for extra punishment)