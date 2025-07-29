# 🛍️ Microservices: Python + Flask + Docker

This is a mini microservices project built using **Python**, **Flask**, and **Docker**. It demonstrates how to run multiple independent services (user, product, and order services) and communicate between them using REST APIs and Docker networking.

## 📁 Project Structure

microservices-demo/
│
├── user-service/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── product-service/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── order-service/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
└── docker-compose.yml


---

## 🔧 Requirements

- Docker installed (https://www.docker.com/)
- Docker Compose installed (https://docs.docker.com/compose/)

No need to install Python or Flask locally — everything runs in Docker.

---

## 🚀 How to Start the Project

### 🛠 1. Clone the Repository

```bash
git clone https://github.com/your-username/microservices-demo.git
cd microservices-demo
docker-compose up --build
```

## 🌐 Available Endpoints

Service	            URL	                                        Description
User Service	      http://localhost:5000/users	                Returns mock user data
Product             Service	http://localhost:5001/products	    Returns product catalog
Order Service	      http://localhost:5002/orders	              Combines user + product

## 🛑 How to Stop the Services

When you're done, stop the containers with:

```bash
docker-compose down
```

To rebuild a single service (e.g. order-service) after changes:

```bash
docker-compose build order-service
```

To restart it:

```bash
docker-compose up order-service
```

## 🛠 Technologies Used
Python 3.9
Flask (for API services)
Docker
Docker Compose
RESTful APIs