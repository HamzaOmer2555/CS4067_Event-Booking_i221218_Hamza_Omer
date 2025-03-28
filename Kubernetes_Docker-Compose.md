# Event Booking Microservices Application

## 🌟 Overview
This project is a microservices-based **Online Event Booking System** built using:
- **FastAPI** for backend APIs
- **PostgreSQL** & **MongoDB** as databases
- **Docker** for containerization
- **Kubernetes** for orchestration and deployment

It supports user registration and login, event creation by admins, booking events, and user notifications.

---

## 🚀 Features & Functionality
### User Service
- **Registration** (`/register`): Allows new users to register.
- **Login** (`/login`): Returns JWT token upon successful login.
- **Get Events** (`/events`): Returns events list from Event service.
- **Book Event** (`/book`): Creates a booking for the logged-in user.
- **Get Notifications** (`/notifications/{email}`): Fetches notifications for the user.

### Event Service
- **Create Event** (`/events`): Admin-only endpoint to create new events.
- **Get Events** (`/events`): Fetch all events.

### Booking Service
- **Create Booking**: Receives requests via user-service to book events.
- Stores booking in PostgreSQL.

### Notification Service
- **Add Notification**: Adds notification for a user when an event is booked.
- **List Notifications**: Fetches user-specific notifications.

---

## 📂 Project Structure
```
.
├── user-service/
├── event-service/
├── booking-service/
├── notification-service/
├── kubernetes_manifests/
│   ├── namespace.yaml
│   ├── deployment-service-user.yaml
│   ├── deployment-service-event.yaml
│   ├── deployment-service-booking.yaml
│   ├── deployment-service-notification.yaml
│   ├── deployment-db-user.yaml
│   ├── deployment-db-event.yaml
│   ├── deployment-db-booking.yaml
│   ├── deployment-db-notification.yaml
│   ├── configmap-user.yaml
│   ├── secret-user.yaml
│   ├── configmap-event.yaml
│   ├── secret-event.yaml
│   ├── configmap-booking.yaml
│   ├── secret-booking.yaml
│   ├── configmap-notification.yaml
│   ├── secret-notification.yaml
│   ├── ingress.yaml
├── frontend/
│   └── index.html
```

---

## 🚫 Microservice Isolation
Each microservice is fully isolated with its own:
- **Container**
- **Database** (PostgreSQL or MongoDB)
- **ConfigMap** for environment variables
- **Secret** for passwords and sensitive data

---

## 🌐 Kubernetes Infrastructure
### Namespace
All resources are created under:
```yaml
Namespace: online-event-booking-hamza-omer
```

### Deployments & Services
Each microservice has a dedicated deployment and service (internal or external):
- **User Service**: Exposed externally
- **Event / Booking / Notification Services**: Internal only

### Databases
- **user-service-db**: PostgreSQL
- **event-service-db**: MongoDB
- **booking-service-db**: PostgreSQL
- **notification-service-db**: MongoDB

### ConfigMaps & Secrets
Environment variables and database credentials are stored securely via:
- **ConfigMaps** for hostnames, ports, database names, etc.
- **Secrets** for usernames and passwords (base64-encoded)

### Ingress
Nginx Ingress routes traffic:
```yaml
/api/users     -> user-service
/api/events    -> event-service
/api/bookings  -> booking-service
/api/notify    -> notification-service
```

---

## 🚫 Security
- JWT tokens are used for authentication
- Admin is hardcoded by email: `hamza.omer.zaki@gmail.com`
- Passwords are sent securely
- Only `user-service` is accessible to frontend users

---

## 📁 Frontend
A basic HTML + JavaScript interface:
- Register/Login user
- View events
- Book event
- View notifications
- Create event (admin only)

Run by simply opening `index.html` in a browser or hosting via NGINX.

---

## 🚧 Running the System
### 1. Apply Namespace
```bash
kubectl apply -f kubernetes_manifests/namespace.yaml
```

### 2. Apply ConfigMaps & Secrets
```bash
kubectl apply -f kubernetes_manifests/configmap-*.yaml
kubectl apply -f kubernetes_manifests/secret-*.yaml
```

### 3. Apply Database Deployments
```bash
kubectl apply -f kubernetes_manifests/deployment-db-*.yaml
```

### 4. Apply Microservice Deployments
```bash
kubectl apply -f kubernetes_manifests/deployment-service-*.yaml
```

### 5. Apply Ingress
```bash
kubectl apply -f kubernetes_manifests/ingress.yaml
```

### 6. Test Application
- Get ingress IP:
  ```bash
  kubectl get ingress -n online-event-booking-hamza-omer
  ```
- Access `http://localhost/api/users/...` from frontend HTML

---

## ⚡ Technologies Used
- **FastAPI** (Python)
- **MongoDB** (v6)
- **PostgreSQL** (v15)
- **Docker & Docker Compose** (for local testing)
- **Kubernetes** (k8s native deployment)
- **Nginx Ingress** (for routing)

---

## ✅ Status
**Fully functional** with support for:
- Auth
- Admin-only event creation
- Cross-service communication
- Microservice deployment in Kubernetes

---

## 🎊 Author
**Hamza Omer Zaki**
i221218@nu.edu.pk
