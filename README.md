# KJW | Building Cloud-Native Systems

Designing and implementing cloud-native platforms across application, Kubernetes, and infrastructure layers.  
From distributed workloads and GitOps delivery to reproducible AWS infrastructure with Terraform.

---

## Core Focus

- Kubernetes Job-based distributed workloads
- Stateless backend architecture
- GitOps (Argo CD) and CI/CD automation
- AWS and Terraform-based infrastructure design
- Reproducible and observable systems

---

## Tech Stack

### Core

<p>
  <img src="https://img.shields.io/badge/Python-151515?style=for-the-badge&logo=python&logoColor=3776AB" alt="Python">
  <img src="https://img.shields.io/badge/Flask-151515?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/MySQL-151515?style=for-the-badge&logo=mysql&logoColor=4479A1" alt="MySQL">
  <img src="https://img.shields.io/badge/Docker-151515?style=for-the-badge&logo=docker&logoColor=2496ED" alt="Docker">
  <img src="https://img.shields.io/badge/Kubernetes-151515?style=for-the-badge&logo=kubernetes&logoColor=326CE5" alt="Kubernetes">
  <img src="https://img.shields.io/badge/Terraform-151515?style=for-the-badge&logo=terraform&logoColor=7B42BC" alt="Terraform">
  <img src="https://img.shields.io/badge/AWS-151515?style=for-the-badge&logo=amazonwebservices&logoColor=FF9900" alt="AWS">
  <img src="https://img.shields.io/badge/GitHub_Actions-151515?style=for-the-badge&logo=github-actions&logoColor=2088FF" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/Argo_CD-151515?style=for-the-badge&logo=argo&logoColor=EF7B4D" alt="Argo CD">
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

Repository:  
[stock-backtest-platform](https://github.com/JJong-03/stock-backtest-platform)

A cloud-native platform that containerizes a legacy Python backtesting engine without modifying its core logic, and executes each run as an isolated Kubernetes Job for parallel processing and horizontal scalability.

I designed and implemented the full lifecycle of the system, from architecture and containerization to CI/CD automation and GitOps deployment.

- Dynamic web-to-Kubernetes Job orchestration
- Stateless architecture by removing local file dependencies
- MySQL-based source of truth
- GitHub Actions to GHCR to Argo CD delivery pipeline
- Traceable execution flow with run_id-based logging

Background:  
This project was originally developed inside a private organization repository. The current repository is a cleaned and documented public version prepared for portfolio presentation.

### 2. AWS Multi-VPC 3-Tier Infrastructure with Terraform

Repository:  
[aws-terraform-multi-vpc](https://github.com/JJong-03/aws-terraform-multi-vpc)

A Terraform-based AWS infrastructure project that provisions a production-like multi-VPC environment with separated application, management, and service networks.

The architecture routes static traffic through CloudFront and S3, dynamic traffic through WAF, ALB, EC2 Nginx, EKS, and Aurora, and isolates admin access through an OpenVPN-based management VPC.

- Multi-VPC network segmentation with VPC peering
- CloudFront and S3 static delivery with WAF-protected dynamic traffic
- ALB to EC2 Nginx to EKS reverse proxy architecture
- Aurora MySQL, ECS Fargate, ECR, Route53, and ACM integration
- Modular Terraform structure with architecture and operations documentation

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
