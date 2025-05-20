#  Runverve User Metrics API

This is a FastAPI backend for storing health metrics (hydration, fatigue, posture) from **Runverve wearable devices**.

---

## ✅ Features

- JWT login (token-based authentication)
- Add device for a user
- Upload health metrics
- Clean structure using controller, service, model, schema
- Swagger UI for testing APIs

---

## Tech Stack
-Python
-Fastapi

1. User Registration API
What it does:
Lets a new user create an account by providing their details.

2. User Login API
What it does:
Allows users to log in with their email and password and get an access token.

3. Add User Matrix API
What it does:
Saves user health data like hydration, fatigue, posture, etc., sent from the wearable device.

4. Get User Matrix API
What it does:
Retrieves the saved health data for the logged-in user.

5. Add Device API
What it does:
Registers a new wearable device for the user.

6. Get Devices API
What it does:
Gets the list of all devices registered by the user.


# Swagger

![Screenshot (62)](https://github.com/user-attachments/assets/04ca3493-f815-4bd9-a9a6-3c9f2dccc957)


