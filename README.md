# 📱 WhatsApp Message Scheduler using Python & Twilio

A simple Python-based WhatsApp Message Scheduler that allows users to schedule a WhatsApp message for a specific date and time.

The project uses the **Twilio WhatsApp API** to send messages and Python's `datetime` and `time` modules to calculate the waiting time before sending the message.

---

## 🚀 Features

- 📲 Send WhatsApp messages using Twilio
- ⏰ Schedule messages for a specific date and time
- 👤 Accept recipient name and WhatsApp number from the user
- 💬 Accept custom message content
- 📅 Supports future date scheduling
- 🕐 Uses 24-hour time format
- ⚠️ Checks whether the scheduled time is in the past
- 🔐 Uses Twilio authentication credentials
- ❌ Handles API/runtime errors using exception handling
- 🖥️ Simple command-line interface

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Twilio API | Sending WhatsApp messages |
| datetime | Date and time processing |
| time | Waiting until scheduled time |
| Exception Handling | Handling API/runtime errors |

---

## 📂 Project Structure

```text
WhatsApp-Message-Scheduler/
│
├── whatsapp_scheduler.py
├── README.md
├── requirements.txt
└── .gitignore
