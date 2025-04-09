# Quote App 🚀

A simple Flask-based application that displays random quotes. This project was containerized using Docker and deployed on a local Kubernetes cluster using Helm charts.

---

## 🔧 Technologies Used

- Python (Flask)
- Docker
- Kubernetes
- Helm
- Minikube / Linux VM

---

## 📦 Setup & Run Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Anushri-VK/quote-app.git
cd quote-app
```

### 2. Dockerize the App

```bash
docker build -t hustlex/quote-app .
docker run -p 5000:5000 hustlex/quote-app
```

### 3. Helm Chart Deployment

```bash
cd quote-app-chart
```

Install the app using Helm:

```bash
helm install quote-release .
```

### 4. Access the App
If running on a VM or Minikube, use port-forwarding:

```bash
kubectl port-forward svc/quote-release-service 5000:5000
```

[Visit the app](http://<vm-ip>:5000)




```
quote-app/
├── app.py                   # Flask app code
├── Dockerfile               # Docker config
├── requirements.txt         # Python dependencies
├── quote-app-chart/         # Helm chart directory
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       ├── deployment.yaml
│       └── service.yaml
└── README.md                # This file
```



✅ **Features Implemented**

- ✅ Flask-based quote app  
- ✅ Dockerized the application  
- ✅ Created Helm chart from scratch  
- ✅ Deployed using Helm on Kubernetes  
- ✅ Verified accessibility via port-forwarding  

📌 Note
This project was done for hands-on learning with Kubernetes and Helm. Debugging steps are not included in this README for clarity.

