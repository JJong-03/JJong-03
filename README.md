# KJW | Cloud-Native Platforms & Infrastructure

애플리케이션, Kubernetes, 인프라 계층을 함께 고려하며  
**실행 격리, 재현성, GitOps, IaC** 중심으로 클라우드 네이티브 시스템을 설계하고 구현합니다.

---

## Core Focus

- Kubernetes Job 기반 분산 실행 구조
- Stateless backend 및 batch workload 아키텍처
- GitOps (Argo CD) 와 CI/CD 자동화
- AWS / GCP 기반 인프라 설계와 Terraform IaC
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

기존에 구현한 백테스트 엔진을 수정 없이 Kubernetes Job으로 외부화해  
**실행 격리, 재현성, 운영 관측성**을 확보한 플랫폼 프로젝트입니다.

- 백테스트 엔진을 Kubernetes Job 단위로 분리해 실행 구조 설계
- Web → Job orchestration 구조 구현
- GitHub Actions, Argo CD, Prometheus, Grafana 기반 배포/관측 체계 구성

### 2. AWS Multi-VPC 3-Tier Infrastructure with Terraform
Repository: [aws-terraform-multi-vpc](https://github.com/JJong-03/aws-terraform-multi-vpc)

Terraform으로 설계·구축한 **multi-VPC 기반 3-tier AWS 인프라 프로젝트**입니다.

- MAIN / MGMT / SERVICE 3개 VPC와 VPC Peering 구성
- CloudFront, WAF, ALB, EKS, Aurora를 포함한 동적/정적 트래픽 경로 설계
- 관리자 접근 경로를 OpenVPN 기반 MGMT VPC로 분리

### 3. GCP GKE GitOps Pipeline
Repository: [gcp-gke-gitops-pipeline](https://github.com/JJong-03/gcp-gke-gitops-pipeline)

Terraform, GKE, GitHub Actions OIDC/WIF, Artifact Registry, Argo CD를 활용해  
**GCP 기반 GitOps pipeline**을 구축하고 실제 배포까지 검증한 프로젝트입니다.

- Terraform으로 GKE 및 관련 인프라 구성
- GitHub Actions + Workload Identity Federation 기반 이미지 빌드/푸시 자동화
- Argo CD sync 및 Ingress 접근 검증

### 4. AWS Terraform Deep Dive
Repository: [aws-terraform-deepdive](https://github.com/JJong-03/aws-terraform-deepdive)

AWS 인프라를 단계적으로 구축한 뒤,  
최종적으로 **Terraform modules + environment separation 구조**로 리팩토링한 프로젝트입니다.

- Networking, Secrets, Messaging, Redis Cache 계층 구성
- modules / environments 구조로 재사용 가능하게 정리
- Terraform 설계 판단과 모듈 체이닝 경험 정리

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
