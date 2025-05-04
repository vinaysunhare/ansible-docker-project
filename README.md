
# Sunhare MediCare Dashboard

A full-stack healthcare dashboard application built with **React**, **Flask**, **PostgreSQL**, and **Nginx**, deployed using **Ansible** and **Docker**. The project includes a CI/CD pipeline with GitHub Actions and monitoring with Prometheus and Grafana.

It allows users to manage patient information dynamically, visualize statistics, and monitor system performance.

---

## 🚀 Features

- **Frontend**: React-based dashboard for viewing patient stats and adding patient information via a form.
- **Backend**: Flask API with endpoints for managing patient data (`GET /patients`, `POST /patients`).
- **Database**: PostgreSQL for storing patient details (name, age, condition).
- **Containerization**: Docker containers for Flask, PostgreSQL, Nginx, Prometheus, and Grafana.
- **Automation**: Ansible playbooks to deploy and manage multi-container setup.
- **CI/CD**: GitHub Actions pipeline for automated testing and deployment.
- **Monitoring**: Prometheus for metrics collection and Grafana for visualization.
- **Networking**: Custom Docker network (`medicare`) for inter-container communication.

---

## 🧰 Tech Stack

- **Frontend**: React, Tailwind CSS, Chart.js, Axios  
- **Backend**: Flask, Flask-SQLAlchemy, Flask-CORS  
- **Database**: PostgreSQL  
- **Containerization**: Docker  
- **Orchestration**: Ansible  
- **CI/CD**: GitHub Actions  
- **Monitoring**: Prometheus, Grafana, Nginx Prometheus Exporter  
- **Version Control**: Git, GitHub  

---

## 📁 Project Structure

```
ansible-docker-project/
├── ansible-env/
├── roles/
│   └── docker_setup/
│       ├── handlers/
│       │   └── main.yml
│       ├── tasks/
│       │   └── main.yml
│       └── templates/
│           ├── backend/
│           │   ├── app.py
│           │   ├── Dockerfile
│           │   └── requirements.txt
│           └── index.html
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── inventory.yml
├── site.yml
└── README.md
```

---

## 🧾 Prerequisites

- Ubuntu (or compatible Linux distribution)
- Docker
- Python 3 and pip
- Git
- Ansible (in a virtual environment)
- GitHub Account

---

## ⚙️ Setup Instructions

### Step 1: Clone the Repository

```bash
git clone git@github.com:vinaysunhare/ansible-docker-project.git
cd ansible-docker-project
```

### Step 2: Update System and Install Dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip git
```

### Step 3: Create and Activate Virtual Environment

```bash
python3 -m venv ansible-env
source ansible-env/bin/activate
```

### Step 4: Install Ansible

```bash
pip install ansible
```

### Step 5: Run Ansible Playbook

```bash
ansible-playbook -i inventory.yml site.yml --ask-become-pass
```

This will:
- Install Docker
- Create Docker network (`medicare`)
- Deploy containers
- Copy frontend
- Configure monitoring

---

## ✅ Verify Deployment

```bash
docker ps
```

- Frontend: http://localhost:5050  
- Flask API: http://localhost:5000/patients  
- PostgreSQL: Port 5432 (internal)  
- Prometheus: http://localhost:9090  
- Grafana: http://localhost:3000  
- Nginx Exporter: http://localhost:9113  

---

## 📊 Usage

- **Dashboard**: View patient statistics
- **Patients Tab**: Add/view patients via API
- **Appointments Tab**: Static view (extendable)

---

## 🔍 Monitoring

- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (admin/admin)

Add Prometheus as a data source and build dashboards for Flask/Nginx.

---

## 🔁 CI/CD Pipeline

- GitHub Actions workflow at `.github/workflows/ci-cd.yml`
- Trigger with:

```bash
git push origin main
```

---

## 🧪 Troubleshooting

- **Ansible**: Activate venv and install
- **Docker**: Ensure running with `sudo systemctl status docker`
- **Ports**: Ensure no conflicts
- **Flask API**: Check PostgreSQL container logs
- **GitHub**: Ensure SSH key added

---

## 🔮 Future Enhancements

- Add user authentication
- Dynamic appointment scheduling
- Custom metrics
- Cloud deployment via Ansible

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch
3. Commit and push
4. Open a PR

---

## 📜 License

© 2025 Sunhare MediCare Dashboard. All rights reserved.

---

## 📝 Notes

### SSH Key

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
cat ~/.ssh/id_rsa.pub
```

Add to GitHub under Settings > SSH and GPG keys.

Ensure file structure matches Ansible paths. Flask Dockerfile and `requirements.txt` should be inside `roles/docker_setup/templates/backend/`.

Grafana default login is `admin/admin`. Change password after login.