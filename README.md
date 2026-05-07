Team Task Manager 🚀

A Full Stack Team Task Management Web Application developed using Flask, MongoDB, HTML, CSS, and JavaScript.
This application helps teams manage projects and tasks efficiently with authentication, task tracking, and admin-based access control.

🔗 Live Demo

https://team-task-manager-production-a4d6.up.railway.app

💻 GitHub Repository

https://github.com/pavaniprabalika-11/team-task-manager

✨ Features
✅ User Signup & Login Authentication
✅ JWT Token-Based Security
✅ Role-Based Access Control
✅ Admin Dashboard
✅ Create & Manage Projects
✅ Create & Assign Tasks
✅ Task Status Tracking
✅ MongoDB Database Integration
✅ REST API Architecture
✅ Responsive Frontend UI
✅ Railway Cloud Deployment
📌 Task Status Workflow

Tasks can be updated with the following statuses:

🟡 Pending
🔵 In Progress
🟢 Completed
🛠️ Tech Stack
Frontend
HTML
CSS
JavaScript
Backend
Flask
Flask-CORS
Flask-JWT-Extended
Flask-Bcrypt
Database
MongoDB
Deployment
Railway

📂 Project Structure
team-task-manager/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── routes/
│   ├── models/
│   ├── middleware/
│   └── config/
│
├── frontend/
│   ├── index.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── style.css
│   └── script.js
│
└── README.md

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/pavaniprabalika-11/team-task-manager.git

2️⃣ Navigate To Backend
cd backend

3️⃣Install Dependencies
pip install -r requirements.txt

4️⃣ Run Flask Server
python app.py

🔑 API Endpoints
Authentication
Signup
POST /api/auth/signup

Login
POST /api/auth/login

Projects
Create Project
POST /api/projects/create

Get Projects
GET /api/projects/all

Tasks
Create Task
POST /api/tasks/create
Update Task Status
PUT /api/tasks/update-status/<task_id>

📸 Screenshots
<img width="1920" height="1020" alt="Screenshot 2026-05-07 171755" src="https://github.com/user-attachments/assets/7c7a07e0-a8ea-40de-afb4-d186c431be72" />





