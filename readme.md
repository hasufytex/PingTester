# Ping Tester

## Overview

This project monitors ping times to multiple targets (such as routers, Cloudflare, Google), detects spikes in ping times, and logs them. It also displays the results in a formatted table and helps identify network issues like latency spikes.

## Prerequisites

- **Python 3.x**: This project is built using Python. Make sure Python 3.x is installed on your system.
- **Required Libraries**: The project uses tabulate that needs to be installed.

## Setup

### 1. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/hasufytex/PingTester
cd PingTester
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run

```bash
python main.py
```