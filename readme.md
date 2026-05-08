# Cloud-Native DevOps Monitoring Platform



A production-style cloud-native DevOps project demonstrating containerization, reverse proxy architecture, monitoring, caching, Infrastructure as Code, CI/CD automation, and Kubernetes orchestration.



###### Live Demo

Live Application: https://your-app-name.azurewebsites.net

GitHub Repository: https://github.com/yourusername/your-repository-name



### Project Overview



This project was built to simulate a modern DevOps and cloud-native application deployment workflow.



The platform includes:



* Multi-container application architecture
* Reverse proxy routing using Nginx
* Redis-based caching and state management
* Monitoring and observability using Prometheus and Grafana
* CI/CD automation with GitHub Actions
* Infrastructure as Code using Bicep
* Local Kubernetes orchestration using Docker Desktop Kubernetes
* Deployment to Azure App Service



The objective of the project was to gain hands-on experience with production-oriented DevOps concepts including container orchestration, monitoring, scaling, networking, and automated deployments.



### Architecture





&#x20;                   User

&#x20;                     ↓

&#x20;                 Nginx Proxy

&#x20;                     ↓

&#x20;                Flask Backend

&#x20;                     ↓

&#x20;                   Redis



&#x20;      Prometheus ← Metrics Collection

&#x20;             ↓

&#x20;         Grafana Dashboards



### Tech Stack





Category	            Technologies

Backend	                    Flask, Python

Reverse Proxy	            Nginx

Containerization            Docker, Docker Compose

Orchestration	            Kubernetes

Monitoring	            Prometheus, Grafana

Cache Layer	            Redis

Cloud Platform	            Microsoft Azure App Service

Infrastructure as Code	    Bicep

CI/CD	                    GitHub Actions

Version Control	            Git, GitHub

OS \& Environment	    Linux (Ubuntu)



### Key Features



#### Multi-Container Architecture

* Flask backend container
* Nginx reverse proxy container
* Redis cache container
* Container networking using Docker Compose



#### Monitoring \& Observability

* Custom Prometheus metrics endpoint
* Application request monitoring
* Grafana dashboards for metrics visualization
* Real-time monitoring pipeline



#### Kubernetes Deployment

* Kubernetes deployments
* Kubernetes services
* Replica scaling
* Rolling deployment support



#### CI/CD Automation

* Automated GitHub Actions workflows
* Docker image build and push automation
* Deployment workflow integration



#### Infrastructure as Code

* Azure infrastructure provisioning using Bicep
* Reproducible deployment configuration



### Project Structure



azure-devops-project/

│

├── app.py

├── requirements.txt

├── Dockerfile

├── docker-compose.yml

│

├── nginx/

│   └── nginx.conf

│

├── monitoring/

│   └── prometheus.yml

│

├── k8s/

│   ├── deployment.yaml

│   └── service.yaml

│

├── infra/

│   └── main.bicep

│

├── templates/

├── static/

│

└── .github/

&#x20;   └── workflows/



### Running Locally



#### Clone Repository



git clone https://github.com/yourusername/your-repository-name.git

cd your-repository-name



#### Build \& Run Containers



docker compose up --build



### Access Services



Service	        URL

Flask App	http://localhost

Prometheus	http://localhost:9090

Grafana	        http://localhost:3000



Grafana Default Credentials:



Username: admin

Password: admin



### Kubernetes Deployment



#### Enable Kubernetes



Enable Kubernetes in Docker Desktop.



##### Apply Kubernetes Configurations

kubectl apply -f k8s/



#### Verify Pods

kubectl get pods



#### Port Forward Service

kubectl port-forward service/flask-service 8080:80



###### Application URL:

http://localhost:8080



### Monitoring Setup



#### Prometheus Metrics Endpoint

http://localhost/prometheus



#### Grafana Dashboard



Query used:

app\_requests\_total



This metric tracks total application requests.



### Azure Deployment



The application was deployed using:



* Azure App Service
* Containerized deployment
* Environment variables
* Azure monitoring integration



### Infrastructure as Code



Infrastructure provisioning was implemented using Bicep templates.



Deployment command:



az deployment group create \\

&#x20; --resource-group rg-devops-practice \\

&#x20; --template-file infra/main.bicep



### CI/CD Workflow



GitHub Actions pipeline automates:



* Docker image build
* Docker image push
* Deployment workflow execution



Example workflow:



&#x20; build:

&#x20;   runs-on: ubuntu-latest



&#x20;   steps:

&#x20;     - uses: actions/checkout@v3



&#x20;     - name: Login to DockerHub

&#x20;       uses: docker/login-action@v2

&#x20;       with:

&#x20;         username: ${{ secrets.DOCKER\_USERNAME }}

&#x20;         password: ${{ secrets.DOCKER\_PASSWORD }}



&#x20;     - name: Build Image

&#x20;       run: docker build -t yourusername/devops-app:v5 .



&#x20;     - name: Push Image

&#x20;       run: docker push yourusername/devops-app:v5



### Security Improvements

* Non-root container execution
* Reverse proxy isolation
* Environment variable configuration
* Container separation using Docker networking



### Skills Demonstrated

* Cloud Infrastructure
* DevOps Engineering
* Containerization
* Monitoring \& Observability
* Kubernetes Fundamentals
* CI/CD Automation
* Infrastructure as Code
* Reverse Proxy Architecture
* Service Networking
* Linux \& System Operations



### Future Improvements

* Helm integration
* Kubernetes Ingress Controller
* Horizontal Pod Autoscaling
* Terraform migration
* Blue/Green deployments
* Centralized logging stack
* SSL/TLS configuration



### Learning Outcomes



Through this project, I gained practical experience with:



* Deploying and managing containerized applications
* Monitoring distributed systems
* Kubernetes deployments and scaling
* CI/CD automation workflows
* Cloud deployment and infrastructure provisioning
* Production-style DevOps architecture



### Author



Jatin Jawa



LinkedIn: https://linkedin.com/in/jatin-jawa

GitHub: https://github.com/Jatin21012004

Email: jatinjawa18@gmail.com

