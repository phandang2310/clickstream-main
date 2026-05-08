# Redis-Based Real-Time Clickstream Analytics System

## Overview

This project is a lightweight real-time clickstream analytics system built with **FastAPI** and **Redis**.

The system captures user interaction events, stores recent events in memory for fast access, and includes a Redis-based analytics service for event statistics and timeline processing.

It was developed as part of the **Modern Database Applications** course to demonstrate practical NoSQL database design using Redis.

---

## Features

* Real-time event tracking
* FastAPI backend API
* Lightweight in-memory event buffer
* Redis analytics service
* Event statistics aggregation
* Event timeline ordering
* Static frontend interface
* Cross-origin request support

---

## Technology Stack

### Backend

* Python 3
* FastAPI
* Uvicorn

### Database

* Redis
* Redis AsyncIO

### Frontend

* HTML
* JavaScript
* Static files served by FastAPI

---

## Project Structure

```text
clickstream/
│
├── app/
│   ├── core/
│   │   ├── redis_client.py
│   │
│   ├── services/
│   │   └── analytics.py
│   │
│   ├── static/
│   │   └── index.html
│   │
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## System Architecture

Frontend
↓
FastAPI API
↓
Event Buffer (`events[]`)
↓
Analytics Response

Redis Analytics Layer

* Event Hash Storage
* Event Timeline
* Event Statistics

---

## API Endpoints

### Home Page

**GET /**

Returns the frontend interface.

---

### Track Event

**POST /track**

Receives event data as JSON.

Example request:

```json
{
  "event_type": "click",
  "element": "submit_button"
}
```

Example response:

```json
{
  "status": "tracked"
}
```

---

### Analytics

**GET /analytics**

Returns recent tracked events.

Example response:

```json
{
  "events": [...]
}
```

---

## Redis Analytics Service

The project includes a Redis analytics layer that supports:

### Save Event

Stores event metadata in Redis Hashes.

### Timeline Ordering

Stores events in Redis Sorted Sets.

### Event Statistics

Tracks event frequency using Redis Hash counters.

---

## Installation

### 1. Clone the repository

```bash
git clone <repository_url>
cd clickstream
```

---

### 2. Create virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Start Redis

Make sure Redis is running locally.

Default connection:

```text
redis://localhost:6379
```

---

### 5. Run the application

```bash
python -m uvicorn app.main:app --reload
```

---

## Access the Application

Frontend:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Current Implementation Notes

The current implementation uses a hybrid architecture:

### Active Flow

Events are stored in an in-memory Python list.

### Redis Layer

Redis analytics functions are implemented separately for scalable event processing.

Future versions can directly connect `/track` to:

```python
AnalyticsService.save_event()
```

to enable full Redis-based event persistence.

---

## Future Improvements

* Full Redis integration
* WebSocket live updates
* Dashboard visualization improvements
* Historical analytics storage
* Redis clustering

---

## Course Information

**Course:** Modern Database Applications

**Project Type:** Redis NoSQL Database Application

---

## Authors

[Your Name]
[Student ID]

[Group Members]
