# Rewards System Web App with Django, Celery, and Redis

This project is a Django web application where users can sign up, log in, view tasks, and upload screenshots. It includes a periodic task using Celery to download ISINs every 24 hours.

## Features

- **User Authentication**: Users can sign up, log in, and view their profiles.
- **Admin Panel**: Admins can add apps and assign points to tasks.
- **Task Management**: Users can view tasks, complete them, and upload screenshots.
- **Periodic Task**: A Celery worker downloads ISINs every 24 hours.
- **REST API**: API endpoints for managing users, apps, tasks, and screenshots.
- **Docker**: Containerization of the application (optional).

---

## Problem Set 3: Solution

### Question A: Scheduling Periodic Tasks with Celery and Redis

We use **Celery** for task scheduling, and **Redis** as the message broker. Celery is a powerful distributed task queue that can handle millions of tasks.

#### Why Celery?

- **Scalability**: Can handle large volumes of tasks efficiently.
- **Distributed**: Tasks can be distributed across multiple workers.
- **Reliable**: Supports retries, task scheduling, and result storage.

### Setup for Periodic Tasks

#### Step 1: Install Celery and Redis

```bash
pip install celery redis
