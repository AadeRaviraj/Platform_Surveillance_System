# Automated Platform Surveillance System — Python Automation Project

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Type](https://img.shields.io/badge/Type-Automation%20Script-red)
![Library](https://img.shields.io/badge/Library-psutil-yellow)
![Feature](https://img.shields.io/badge/Feature-Email%20Report-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

An automated system monitoring tool built in Python that continuously tracks real-time system performance metrics — CPU, RAM, Disk, Network, and all running processes. It generates structured timestamped log files and automatically emails the report to a configured recipient at a scheduled time interval.

---

## Problem Statement

System administrators and developers need to monitor machine health over time. Manually checking CPU, memory, disk, and process details is tedious and impossible to do continuously. This project automates the entire surveillance pipeline — collecting system data, writing structured logs, and emailing reports — all running on a set schedule without any manual intervention.

---

## Project Structure

```
Automated_Platform_Surveillance_System/
│
├── PlatformSurveillance.py     # Main script — scan, log, and email system reports
├── memoryprocess.py            # Standalone utility to display top 10 memory processes
├── LogfileName.log             # Temporary process report file attached to emails
│
├── Demo/                       # Auto-created folder storing all timestamped log files
│   ├── Platform_2026-02-13_13-31-09.log
│   ├── Platform_2026-02-14_02-54-37.log
│   └── Platform_2026-02-14_11-32-05.log
│
├── .env                        # Environment variables (credentials — do not push to GitHub)
└── README.md
```

---

## Key Features

| Feature | Description |
|---------|-------------|
| CPU Monitoring | Records real-time CPU usage percentage at the time of each log run |
| RAM Monitoring | Records total RAM usage percentage using `psutil.virtual_memory()` |
| Disk Monitoring | Reports used percentage for every mounted disk partition |
| Network Monitoring | Records total bytes sent and received since system boot |
| Process Scanning | Collects PID, name, username, status, start time, CPU %, and memory % for all processes |
| Thread Monitoring | Records thread count and thread list for every running process |
| Open File Monitoring | Records open file handle count per process (Access Denied handled gracefully) |
| Top 10 Memory Processes | Identifies and logs the top 10 processes consuming the most RAM (RSS) |
| Timestamped Log Files | Creates a new structured log file for every scheduled run |
| Email Report | Sends the log file as an email attachment automatically after each run |
| Scheduled Execution | Runs automatically at a user-defined interval using the `schedule` library |

---

## Functions Overview

| Function | File | Description |
|----------|------|-------------|
| `ProcessScan` | PlatformSurveillance.py | Scans all running processes and returns a list of detailed info dictionaries |
| `CreateLog` | PlatformSurveillance.py | Creates a full system report log file with all metrics and process data |
| `send_mail` | PlatformSurveillance.py | Generates a log, writes a process report, and emails it via Gmail SMTP |
| `main` | PlatformSurveillance.py | Entry point — handles CLI arguments and starts the scheduler |
| `RealmemoryUse` | memoryprocess.py | Standalone utility — displays top 10 memory-consuming processes |

---

## How It Works — Step by Step

**Step 1 — Process Scan**
All running processes are scanned using `psutil.process_iter()`. A warm-up pass runs first to allow `psutil` to calculate accurate CPU percentages. Each process record includes PID, name, status, CPU %, RAM %, RSS, VMS, thread count, and open file handles.

**Step 2 — System Snapshot**
CPU usage, RAM usage, disk usage per partition, and network I/O statistics are all collected using `psutil` at the time of the run.

**Step 3 — Write Log File**
A structured log file is created inside the configured folder with a timestamped name like `Platform_2026-02-14_11-32-05.log`. It contains all system metrics and full process data divided into clearly labelled sections.

**Step 4 — Send Email**
A process-level report is written to `LogfileName.log` and sent as an email attachment via Gmail SMTP SSL on port 465. The email is sent to the receiver address provided as a command-line argument.

**Step 5 — Repeat on Schedule**
All of the above runs automatically every N minutes. The script keeps running in an infinite loop, triggering the full pipeline at each scheduled interval.

---

## Log File Sections

Each log file generated in the `Demo/` folder contains the following sections:

| Section | Contents |
|---------|----------|
| System Report Header | Timestamp of the log run |
| CPU Usage | Overall CPU usage percentage |
| RAM Usage | Overall RAM usage percentage |
| Disk Usage Report | Usage percentage per disk partition |
| Network Usage Report | Total MB sent and received |
| Process Report | PID, name, username, status, start time, CPU %, memory % per process |
| Thread Monitoring | Thread count and thread list per process |
| File Monitoring | Open file handle count per process |
| Top 10 Memory Processes | RSS, VMS, and memory % for the 10 highest RAM-consuming processes |

---

## Command Line Usage

```bash
# Show help
python PlatformSurveillance.py --h

# Show usage instructions
python PlatformSurveillance.py --u

# Start surveillance — log every 10 minutes, save to 'Demo' folder, email to receiver
python PlatformSurveillance.py 10 Demo receiver@gmail.com
```

Press `Ctrl + C` to stop the script.

---

## Email Configuration

The email feature uses Gmail SMTP SSL with a Google App Password. To configure it for your own account:

1. Go to your Google Account settings
2. Enable 2-Step Verification
3. Go to Security and generate an App Password
4. Replace `sender_email` and `app_passward` in `PlatformSurveillance.py` with your credentials
 

---

## Tech Stack

- Python 3
- `psutil` — system and process monitoring (CPU, RAM, Disk, Network, Processes)
- `smtplib` and `email` — sending email with log file attachment via Gmail SMTP SSL
- `os` — directory creation and file path operations
- `schedule` — scheduling the surveillance to run at set time intervals
- `time` — timestamps for log file names and log entries
- `sys` — reading command-line arguments

---

## How to Run

1. Clone this repository
2. Install the required libraries:
   ```bash
   pip install psutil schedule
   ```
3. Configure your email credentials in `PlatformSurveillance.py`
4. Run the script:
   ```bash
   python PlatformSurveillance.py 10 Demo receiver@gmail.com
   ```

---

## Key Concepts Covered

- Real-Time System Monitoring using `psutil`
- Process Scanning with Exception Handling (`NoSuchProcess`, `AccessDenied`, `ZombieProcess`)
- CPU Warm-up for Accurate Percentage Readings
- Epoch Timestamp Conversion to Human-Readable Format
- Structured Log File Generation
- Thread and Open File Handle Monitoring
- Top N Process Sorting using `sorted()` and `lambda`
- Email Automation with Attachments (`smtplib`, `EmailMessage`)
- Gmail SMTP SSL Authentication with App Password
- Scheduled Task Execution (`schedule` library)
- Command Line Argument Handling (`sys.argv`)

 

---

## Author

**Raviraj Aade**

Built as a Python Automation Project to understand real-time system monitoring, process-level data collection, structured log generation, email automation, and scheduled task execution using pure Python.
