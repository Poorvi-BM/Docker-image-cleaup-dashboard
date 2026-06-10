# 🐳 Docker Image Cleanup Dashboard

## 📌 Project Overview

Docker Image Cleanup Dashboard is a Flask-based DevOps utility that helps users monitor, analyze, and optimize Docker image storage. The system identifies unused, duplicate, and dangling Docker images, provides storage analytics, tracks cleanup history, and offers intelligent cleanup recommendations to improve Docker host maintenance.

The application communicates directly with Docker Engine using the Docker SDK for Python and provides a modern web-based dashboard for Docker image management.

---

# 🎯 Problem Statement

Docker environments often accumulate unused and duplicate images over time, consuming significant disk space and affecting system maintenance.

This project provides an intelligent dashboard to:

* Detect unused Docker images
* Detect duplicate Docker images
* Detect dangling Docker images
* Monitor Docker image storage usage
* Track cleanup operations
* Generate cleanup reports
* Improve Docker resource utilization

---

# ✨ Features

### Image Management

* View all Docker images
* Delete individual Docker images
* Bulk cleanup of unused Docker images
* Detect duplicate Docker images
* Detect dangling Docker images

### Analytics Dashboard

* Total Docker Images
* Total Storage Usage
* Unused Images Count
* Duplicate Images Count
* Space Saved Tracker
* Docker Health Score
* Storage Analytics Chart

### Smart Monitoring

* Docker Engine Status
* Running Containers Count
* Stopped Containers Count
* Smart Cleanup Recommendations
* Potential Storage Recovery Analysis

### Reporting

* Cleanup History Tracking
* SQLite Database Storage
* CSV Report Export

### Security

* User Login Authentication
* Session Management

---

# 🛠 Technology Stack

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Chart.js

## Backend

* Python
* Flask

## Database

* SQLite

## DevOps

* Docker SDK for Python
* Docker Engine

---

# 🏗 System Architecture

```text
User
 │
 ▼
Flask Dashboard
 │
 ▼
Docker SDK for Python
 │
 ▼
Docker Engine
 │
 ▼
Docker Images & Containers
```

---

# 📂 Project Structure

```text
docker-image-cleanup-dashboard/

│
├── app.py
├── requirements.txt
├── cleanup.db
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   └── history.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/docker-image-cleanup-dashboard.git

cd docker-image-cleanup-dashboard
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install flask docker
```

---

## Start Docker Desktop

Ensure Docker Desktop is running before launching the application.

Verify Docker:

```bash
docker ps
```

---

## Run Application

```bash
python app.py
```

Application URL:

```text
http://127.0.0.1:5000
```

---

# 🔐 Demo Login Credentials

```text
Username: admin

Password: admin123
```

---

# 📊 Dashboard Modules

### Login Module

Provides secure user authentication.

### Dashboard Module

Displays:

* Total Images
* Total Storage
* Unused Images
* Duplicate Images
* Space Saved
* Health Score

### Analytics Module

Provides storage usage visualization through charts.

### Cleanup Module

Allows:

* Single Image Deletion
* Unused Image Cleanup

### History Module

Stores cleanup operations with:

* Image Name
* Image ID
* Storage Freed
* Deleted Time

### Report Module

Exports cleanup records as CSV reports.

---

# 🚀 How To Test

Pull sample images:

```bash
docker pull nginx
docker pull ubuntu
docker pull postgres
docker pull mysql
docker pull redis
docker pull python
docker pull node
```

Verify:

```bash
docker images
```

Open Dashboard:

```text
http://127.0.0.1:5000/dashboard
```

Perform cleanup operations and verify updates in History.

---

# 📈 Future Enhancements

* Bulk Image Deletion
* Image Restore Functionality
* Docker Container Monitoring
* Kubernetes Integration
* Email Alerts
* AI-Based Cleanup Recommendations
* Cloud Deployment

---

# 🎓 Academic Information

### Project Title

Docker Image Cleanup Dashboard

### Domain

DevOps / Cloud Computing

### Developed Using

Python, Flask, Docker SDK, SQLite, Bootstrap, Chart.js

---

# 👩‍💻 Developed By

Poorvi

Department of Computer Science and Engineering

2026

---

# 📄 License

This project is developed for educational and academic purposes.
