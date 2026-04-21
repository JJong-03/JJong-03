# KJW | Building Cloud-Native Platforms

Designing and implementing cloud-native systems across application, Kubernetes, and infrastructure layers.  
Focused on reproducible execution, GitOps delivery, and AWS/GCP infrastructure with Terraform.

---

## Core Focus

- Kubernetes Job-based distributed workloads
- Stateless backend and batch execution architecture
- GitOps (Argo CD) and CI/CD automation
- AWS/GCP infrastructure design with Terraform
- Reproducible and observable systems

---

## Tech Stack

### Core

<p>
  <img src="https://img.shields.io/badge/Python-151515?style=for-the-badge&logo=python&logoColor=3776AB" alt="Python">
  <img src="https://img.shields.io/badge/Flask-151515?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/MySQL-151515?style=for-the-badge&logo=mysql&logoColor=4479A1" alt="MySQL">
  <br/>
  <img src="https://img.shields.io/badge/Docker-151515?style=for-the-badge&logo=docker&logoColor=2496ED" alt="Docker">
  <img src="https://img.shields.io/badge/Kubernetes-151515?style=for-the-badge&logo=kubernetes&logoColor=326CE5" alt="Kubernetes">
  <img src="https://img.shields.io/badge/GitHub_Actions-151515?style=for-the-badge&logo=github-actions&logoColor=2088FF" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/Argo_CD-151515?style=for-the-badge&logo=argo&logoColor=EF7B4D" alt="Argo CD">
  <br/>
  <img src="https://img.shields.io/badge/Amazon%20AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white&v=2" alt="AWS">
  <img src="https://img.shields.io/badge/GCP-151515?style=for-the-badge&logo=googlecloud&logoColor=4285F4" alt="GCP">
  <img src="https://img.shields.io/badge/Terraform-151515?style=for-the-badge&logo=terraform&logoColor=7B42BC" alt="Terraform">
</p>

### Foundation

<p>
  <img src="https://img.shields.io/badge/Linux-151515?style=for-the-badge&logo=linux&logoColor=FCC624" alt="Linux">
  <img src="https://img.shields.io/badge/Networking-151515?style=for-the-badge" alt="Networking">
  <img src="https://img.shields.io/badge/C-151515?style=for-the-badge&logo=c&logoColor=00599C" alt="C">
</p>

---

## Featured Projects

### 1. Kubernetes-based Stock Backtesting Platform
Repository: [stock-backtest-platform](https://github.com/JJong-03/stock-backtest-platform)

A cloud-native platform that runs an existing Python backtesting engine as isolated Kubernetes Jobs for scalable and reproducible execution.

- Externalized the engine into Kubernetes Jobs without modifying core logic
- Built web-to-job orchestration for isolated batch execution
- Added GitOps delivery and observability with Argo CD, Prometheus, and Grafana

### 2. AWS Multi-VPC 3-Tier Infrastructure with Terraform
Repository: [aws-terraform-multi-vpc](https://github.com/JJong-03/aws-terraform-multi-vpc)

A production-like AWS infrastructure project built with Terraform across multiple VPCs for application, management, and service workloads.

- Designed MAIN / MGMT / SERVICE VPC topology with peering
- Built CloudFront + WAF + ALB + EKS + Aurora traffic flow
- Separated admin access through OpenVPN-based management routing

### 3. GCP GKE GitOps Pipeline
Repository: [gcp-gke-gitops-pipeline](https://github.com/JJong-03/gcp-gke-gitops-pipeline)

A GCP-based GitOps pipeline project using Terraform, GKE, GitHub Actions OIDC/WIF, Artifact Registry, and Argo CD.

- Provisioned GKE and supporting infrastructure with Terraform
- Implemented image build/push with GitHub Actions and WIF
- Verified rollout, Ingress access, and Argo CD sync/health state

### 4. AWS Terraform Deep Dive
Repository: [aws-terraform-deepdive](https://github.com/JJong-03/aws-terraform-deepdive)

A Terraform deep dive project that incrementally built AWS infrastructure and refactored it into reusable modules and environment-separated layouts.

- Built networking, secrets, messaging, and Redis cache layers
- Structured reusable modules with dev/prod environments
- Practiced module chaining, state separation, and infrastructure design decisions

---

## GitHub Stats

<div align="center">
<img src="https://github-readme-stats-eight-theta.vercel.app/api?username=JJong-03&show_icons=true&theme=transparent&hide_border=true&title_color=326CE5&icon_color=326CE5&text_color=888888&v=1" height="150" alt="GitHub Stats" />
<img src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=JJong-03&layout=compact&theme=transparent&hide_border=true&title_color=326CE5&text_color=888888&v=1" height="150" alt="Top Languages" />
</div>

---

## Contact

<p>
  <a href="mailto:jowon7602@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white"/>
  </a>
</p>
