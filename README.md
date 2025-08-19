
# 🛍️ FastAPI Products API

A simple **FastAPI** application for managing products.  
This API supports **CRUD operations** (Create, Read, Update, Delete) with in-memory storage using Python dictionaries.

---

## 🚀 Features

- **Create** a product ✅
- **Retrieve** all products ✅
- **Retrieve** a single product by ID ✅
- **Update** an existing product ✅
- **Delete** a product ✅
- Automatic **400 Bad Request** and **404 Not Found** error handling
- Returns **204 No Content** on successful deletion

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/fastapi-products-api.git
cd fastapi-products-api
```

### 2️⃣ Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the FastAPI server with **Uvicorn**:

```bash
uvicorn server:app --reload
```

* The app will run at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
* Open the interactive API docs at: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 📌 API Endpoints

### **1. Create a product**

**POST** `/products`

```json
{
  "name": "Laptop",
  "description": "A powerful gaming laptop",
  "price": 1500
}
```

**Responses:**

* `200 OK` → Returns the created product
* `400 Bad Request` → Missing name or invalid price

---

### **2. Get all products**

**GET** `/products`

```json
{
  "7d89f09a-9f7a-4c3c-bb9d-d731a5bfae1d": {
    "id": "7d89f09a-9f7a-4c3c-bb9d-d731a5bfae1d",
    "name": "Laptop",
    "description": "A powerful gaming laptop",
    "price": 1500,
    "created_at": "2025-08-19T10:30:00",
    "updated_at": "2025-08-19T10:30:00"
  }
}
```

---

### **3. Get product by ID**

**GET** `/products/{id}`
**Responses:**

* `200 OK` → Returns the product
* `404 Not Found` → Product does not exist

---

### **4. Update product**

**PUT** `/products/{id}`

```json
{
  "name": "Updated Laptop",
  "price": 1400
}
```

**Responses:**

* `200 OK` → Returns the updated product
* `404 Not Found` → Product not found

---

### **5. Delete product**

**DELETE** `/products/{id}`
**Responses:**

* `204 No Content` → Successfully deleted
* `404 Not Found` → Product not found

---

## 🛠️ Technologies Used

* **Python 3.10**
* **FastAPI** — Web framework
* **Uvicorn** — ASGI server
* **Dataclasses** — To manage product data

---

## 📄 License

This project is licensed under the **MIT License**.
You’re free to use, modify, and distribute it.


---

