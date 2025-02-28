# Event Booking Microservices Application

## 📌 Overview
The **Event Booking Microservices Application** is a distributed system that enables users to register, browse events, book tickets, and receive notifications. The application follows a **microservices architecture**, with each service handling a distinct responsibility and communicating through **REST APIs**.

### **Tech Stack Used**
- **Backend:** FastAPI (Python), SQLAlchemy, MongoDB, PostgreSQL
- **Frontend:** React.js (Vite)
- **Database:** PostgreSQL (User & Booking Service), MongoDB (Event & Notification Service)
- **Authentication:** JWT (JSON Web Tokens)
- **Containerization:** Docker

---
## 📌 Microservices Overview
The system consists of the following **microservices**, each running independently:

### **1️⃣ User Service (`user-service`)**
- Handles **user registration, authentication (JWT), and profile management**.
- **Database:** PostgreSQL
- **Endpoints:**
  - `POST /register` → Registers a new user
  - `POST /login` → Logs in a user and returns a JWT token
  - `GET /users/{user_id}` → Fetches user details
  - `GET /users` → Fetches all registered users

### **2️⃣ Event Service (`event-service`)**
- Manages event creation and availability tracking.
- **Database:** MongoDB
- **Endpoints:**
  - `POST /events` → Creates a new event
  - `GET /events` → Retrieves all available events
  - `GET /events/{event_id}` → Retrieves event details
  - `PUT /events/{event_id}/update_tickets` → Updates available tickets after a booking

### **3️⃣ Booking Service (`booking-service`)**
- Manages ticket bookings for registered users.
- **Ensures ticket availability before booking** and **updates event availability**.
- **Database:** PostgreSQL
- **Endpoints:**
  - `POST /bookings` → Creates a new booking (verifies user & ticket availability)
  - `GET /bookings` → Retrieves all bookings

### **4️⃣ Notification Service (`notification-service`)**
- Handles **email notifications** and **in-app notifications** for bookings.
- **Database:** MongoDB
- **Endpoints:**
  - `POST /notifications` → Sends a notification (email + stores in MongoDB)
  - `GET /notifications/{user_email}` → Retrieves all notifications for a user

### **5️⃣ Frontend Service (`frontend-service`)**
- Provides a **user-friendly UI** for interacting with the system.
- **Built with React.js + Vite**.
- Communicates with all backend microservices via REST API.

---
## 📌 Microservices Communication
### **User Authentication Workflow**
1. **User registers (`POST /register`)** → Stored in User Service.
2. **User logs in (`POST /login`)** → JWT token is issued.
3. **Frontend stores the token** → Used for authentication in all API requests.

### **Event Booking Workflow**
1. User logs in and **browses available events (`GET /events`)**.
2. User selects an event and **creates a booking (`POST /bookings`)**.
3. **Booking Service validates:**
   - **Checks user ID via User Service** (`GET /users/{user_id}`)
   - **Checks ticket availability via Event Service** (`GET /events/{event_id}`)
   - If available, **reduces ticket count** (`PUT /events/{event_id}/update_tickets`).
4. **Notification Service sends an email & stores a notification**.
5. User can **view past bookings and notifications (`GET /notifications/{user_email}`)**.

---
## 📌 How to Use the Application
### **1️⃣ Setting Up the Microservices**
#### **Using Docker Compose (Recommended)**
```bash
docker-compose up --build
```
This will automatically start all microservices **(User, Event, Booking, Notification, and Frontend)**.

#### **Manual Startup**
Start each service individually:
```bash
# User Service
uvicorn user-service.app:app --reload --host 0.0.0.0 --port 8000

# Event Service
uvicorn event-service.app:app --reload --host 0.0.0.0 --port 8001

# Booking Service
uvicorn booking-service.app:app --reload --host 0.0.0.0 --port 8002

# Notification Service
uvicorn notification-service.app:app --reload --host 0.0.0.0 --port 8003

# Frontend Service
cd frontend-service
npm run dev
```

### **2️⃣ Testing API Endpoints**
- **Swagger UI:** `http://127.0.0.1:<service_port>/docs`
- **Postman/Curl:**
  - Register a user: `POST http://127.0.0.1:8000/register`
  - Login: `POST http://127.0.0.1:8000/login`
  - Get Events: `GET http://127.0.0.1:8001/events`
  - Book a Ticket: `POST http://127.0.0.1:8002/bookings`
  - Get Notifications: `GET http://127.0.0.1:8003/notifications/{user_email}`

### **3️⃣ Using the Frontend**
1. Open `http://localhost:5173`.
2. **Login/Register** as a user.
3. Browse **events, book tickets, and view notifications**.

---
## 📌 Future Enhancements (Optional)
🔹 **Deploy with Kubernetes** (Orchestrate containers efficiently).
🔹 **Implement API Gateway** (Single entry point for all services).
🔹 **WebSockets for Real-Time Notifications** (Faster updates for users).
🔹 **Frontend UI Enhancements** (Material UI, Tailwind CSS).

---
## 📌 Conclusion
This **Event Booking Microservices Application** demonstrates how to build a **scalable, distributed system** with independent services communicating via REST APIs. 🚀

### 🎯 **Key Features:**
✅ **Microservices-based architecture** (Scalability, Fault-tolerance)  
✅ **Secure authentication with JWT**  
✅ **Database interactions with PostgreSQL & MongoDB**  
✅ **Event-driven notifications (Email + In-App)**  
✅ **Containerized & ready for deployment**  

🚀 **Now your system is ready for production!** 🎉

