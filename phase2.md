# Phase 2: CI/CD Pipeline

This document outlines the steps to set up a **CI/CD pipeline** for deploying a Flask app to a remote server using either **GitHub Actions** or **Jenkins**. The pipeline automates building, testing, and deploying the app whenever changes are pushed to the `main` branch.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Workflow Overview](#workflow-overview)
3. [File Arrangement Diagram](#file-arrangement-diagram)
4. [Step-by-Step Guide](#step-by-step-guide)
   - [Option 1: GitHub Actions](#option-1-github-actions)
   - [Option 2: Jenkins](#option-2-jenkins)
5. [Optional: Use Systemd for Better Reliability](#optional-use-systemd-for-better-reliability)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before starting, ensure you have the following:

1. A **GitHub repository** with your Flask app code.
2. A **remote server** (e.g., AWS EC2) with SSH access.
3. An **SSH key pair** for authenticating with the remote server.
4. **Python** and **pip** installed on the remote server.
5. (For Jenkins) A **Jenkins server** set up and running.

---

## Workflow Overview

The CI/CD pipeline performs the following steps:

1. **Build**:
   - Checks out the code.
   - Installs dependencies.
   - Runs unit tests.
2. **Deploy**:
   - Copies the new code to the remote server.
   - Stops the old app (if running).
   - Installs dependencies on the remote server.
   - Starts the new app.

---

## File Arrangement Diagram

Here’s the structure of the repository and remote server:

```
devops-project/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions workflow
├── python-app/
│   ├── app.py                 # Flask application
│   ├── requirements.txt       # Python dependencies
│   └── test_app.py            # Unit tests
├── Jenkinsfile                # Jenkins pipeline script
└── README.md                  # Project documentation

Remote Server:
/home/ec2-user/
└── app/
    ├── app.py                 # Deployed Flask app
    ├── requirements.txt       # Installed dependencies
    └── app.log                # Application logs
```

---

## Step-by-Step Guide

### Option 1: GitHub Actions

#### Step 1: Set Up GitHub Actions

1. Go to your GitHub repository > **Settings** > **Secrets and variables** > **Actions**.
2. Add the following secrets:
   - **`SSH_PRIVATE_KEY`**: Your SSH private key for accessing the remote server.
   - **`KNOWN_HOSTS`**: The `known_hosts` entry for your server (run `ssh-keyscan <server-ip>` to generate this).

#### Step 2: Create the GitHub Actions Workflow

1. In your repository, create a `.github/workflows/ci-cd.yml` file with the following content:
   ```yaml
   name: CI/CD Pipeline

   on:
     push:
       branches:
         - main

   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout code
           uses: actions/checkout@v3

         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.x'

         - name: Install dependencies
           run: |
             cd python-app
             python -m pip install --upgrade pip
             pip install -r requirements.txt

         - name: Run unit tests
           run: |
             cd python-app
             python -m unittest test_app.py

     deploy:
       needs: build
       runs-on: ubuntu-latest
       steps:
         - name: Checkout code
           uses: actions/checkout@v3

         - name: Install SSH key
           uses: shimataro/ssh-key-action@v2
           with:
             key: ${{ secrets.SSH_PRIVATE_KEY }}
             known_hosts: ${{ secrets.KNOWN_HOSTS }}

         - name: Deploy to staging server
           run: |
             scp -r python-app ec2-user@3.83.174.167:/home/ec2-user/app

             ssh ec2-user@3.83.174.167 << 'EOF'
             cd /home/ec2-user/app
             pkill -f "gunicorn" || true
             pip install -r requirements.txt
             nohup gunicorn --bind 0.0.0.0:5000 app:app > app.log 2>&1 &
             EOF
   ```

#### Step 3: Test the Pipeline

1. Push changes to GitHub and verify the workflow runs successfully.
2. Test the app by accessing `http://<server-ip>:5000`.

---

### Option 2: Jenkins

Refer to the guide for setting up Jenkins similar to the GitHub Actions method.

---

## Optional: Use Systemd for Better Reliability

For better reliability, use **systemd** to run the app as a service.

### Step 1: Create a Systemd Service File

On the remote server, create a service file (`/etc/systemd/system/flask-app.service`):

```ini
[Unit]
Description=Flask App
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/app
ExecStart=/usr/local/bin/gunicorn --bind 0.0.0.0:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

### Step 2: Reload Systemd and Start the Service

```bash
sudo systemctl daemon-reload
sudo systemctl start flask-app
sudo systemctl enable flask-app
```

### Step 3: Update the Deployment Script

Modify the `Deploy to staging server` step to copy files and restart the service:

```yaml
- name: Deploy to staging server
  run: |
    scp -r python-app ec2-user@3.83.174.167:/home/ec2-user/app
    ssh ec2-user@3.83.174.167 "sudo systemctl restart flask-app"
```

---

## Troubleshooting

1. **App Not Running**:

   - Check the logs on the remote server:
     ```bash
     cat /home/ec2-user/app/app.log
     ```
   - Verify the app is bound to `0.0.0.0` and not `127.0.0.1`.

2. **App Not Accessible**:

   - Ensure the EC2 security group allows inbound traffic on port `5000`.
   - Check the server’s firewall rules (e.g., `ufw` or `iptables`).

3. **Deployment Fails**:

   - Check the GitHub Actions or Jenkins logs for errors.
   - Verify the SSH key and `known_hosts` entry are correct.

---

By following this guide, you’ll have a fully automated CI/CD pipeline for deploying your Flask app using either **GitHub Actions** or **Jenkins**.

