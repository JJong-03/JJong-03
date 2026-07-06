# KJW | Cloud-Native Platforms & Infrastructure

애플리케이션, Kubernetes, 인프라 계층을 함께 고려하며  
**실행 격리, 재현성, GitOps, IaC** 중심으로 클라우드 네이티브 시스템을 설계하고 구현합니다.

**Portfolio Website:** [kjw-cloud-portfolio.vercel.app](https://kjw-cloud-portfolio.vercel.app)

---

## Core Focus

- Kubernetes Job 기반 분산 실행 구조
- Stateless backend 및 batch workload 아키텍처
- GitOps (Argo CD) 와 CI/CD 자동화
- AWS / GCP 기반 인프라 설계와 Terraform IaC
- IoT telemetry 수집 → read model 집계 → dashboard 조회 경로 설계
- Reproducible and observable systems

---

## Tech Stack

### Core

<p>
  <img src="https://img.shields.io/badge/Python-151515?style=for-the-badge&logo=python&logoColor=3776AB" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-151515?style=for-the-badge&logo=fastapi&logoColor=009688" alt="FastAPI">
  <img src="https://img.shields.io/badge/Flask-151515?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/MySQL-151515?style=for-the-badge&logo=mysql&logoColor=4479A1" alt="MySQL">
  <img src="https://img.shields.io/badge/PostgreSQL-151515?style=for-the-badge&logo=postgresql&logoColor=4169E1" alt="PostgreSQL">
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

### 1. Aegis-Pi Risk Twin — Multi-Factory Safety Observability Platform

Personal implementation: [aegis-pi/dashboard_vpc](https://github.com/aegis-pi/dashboard_vpc) · Team repo: [msp-team03](https://github.com/Team-msp-architect-2026/msp-team03) · [Detail](https://kjw-cloud-portfolio.vercel.app/projects/aegis-pi-risk-twin)

여러 공장의 센서·AI·인프라 상태를 **Safety Score**로 표준화하고 중앙 dashboard · daily report · Slack alert로 연결한 팀 프로젝트입니다.  
**MSP 최종 프로젝트 발표 최우수팀 수상 (팀 수상, 2026.06)**

- data/dashboard plane 설계·구현 — 개인 구현 저장소 `dashboard_vpc` 기준 (Terraform infra, FastAPI dashboard backend, React dashboard)
- telemetry를 Safety Score로 표준화하는 파이프라인(risk-normalizer, risk-score-engine, data-processor)과 Slack alert notifier 구현
- deployment/control path와 user/read path를 VPC 경계로 분리하고, dashboard 조회는 DynamoDB read model로 사전 집계된 상태만 읽도록 설계

### 2. LawMainRoad (법대로) — Labor-Law RAG & Document Workflow

Repository: [law_main_road_main](https://github.com/2026-moel-datacontest-core/law_main_road_main) · [after_step (RAG 개선)](https://github.com/2026-moel-datacontest-core/after_step) · [Demo](https://www.law-main-road.cloud) · [Detail](https://kjw-cloud-portfolio.vercel.app/projects/law-main-road)

외국인 근로자 등 취약 노동자가 노동 문제를 **한국 노동법 근거와 함께** 정리하도록 돕는 AI 지원 MVP 팀 프로젝트입니다.

- PostgreSQL + pgvector(HNSW) → Vertex AI Gemini grounded answer로 이어지는 법령 RAG 흐름
- citation·context 없는 생성 답변을 제한하는 grounding 경계와 privacy boundary 설계
- 법령 근거 답변 → 지원 문서 초안까지 이어지는 document workflow (기술 구성은 팀 공개 저장소·Wiki 기준)

### 3. Kubernetes-based Stock Backtesting Platform

Repository: [stock-backtest-platform](https://github.com/JJong-03/stock-backtest-platform) · [Detail](https://kjw-cloud-portfolio.vercel.app/projects/stock-backtest-platform)

기존에 구현한 백테스트 엔진을 수정 없이 Kubernetes Job으로 외부화해  
**실행 격리, 재현성, 운영 관측성**을 확보한 개인 프로젝트입니다. **MSP 과정 개인 프로젝트 우수상 수상**

- 백테스트 엔진을 Kubernetes Job 단위로 분리해 실행 구조 설계
- Web → Job orchestration 구조 구현
- GitHub Actions, Argo CD, Prometheus, Grafana 기반 배포/관측 체계 구성

### 4. AWS Multi-VPC 3-Tier Infrastructure with Terraform

Repository: [aws-terraform-multi-vpc](https://github.com/JJong-03/aws-terraform-multi-vpc) · [Detail](https://kjw-cloud-portfolio.vercel.app/projects/aws-terraform-multi-vpc)

Terraform으로 설계·구축한 **multi-VPC 기반 3-tier AWS 인프라 프로젝트**입니다.

- MAIN / MGMT / SERVICE 3개 VPC와 VPC Peering 구성
- CloudFront, WAF, ALB, EKS, Aurora를 포함한 동적/정적 트래픽 경로 설계
- 관리자 접근 경로를 OpenVPN 기반 MGMT VPC로 분리

### 5. GCP GKE GitOps Pipeline

Repository: [gcp-gke-gitops-pipeline](https://github.com/JJong-03/gcp-gke-gitops-pipeline) · [Detail](https://kjw-cloud-portfolio.vercel.app/projects/gcp-gke-gitops-pipeline)

Terraform, GKE, GitHub Actions OIDC/WIF, Artifact Registry, Argo CD를 활용해  
**GCP 기반 GitOps pipeline**을 구축하고 실제 배포까지 검증한 프로젝트입니다.

- Terraform으로 GKE 및 관련 인프라 구성
- GitHub Actions + Workload Identity Federation 기반 이미지 빌드/푸시 자동화
- Argo CD sync 및 Ingress 접근 검증

### 6. AWS Terraform Deep Dive

Repository: [aws-terraform-deepdive](https://github.com/JJong-03/aws-terraform-deepdive) · [Detail](https://kjw-cloud-portfolio.vercel.app/projects/aws-terraform-deepdive)

AWS 인프라를 단계적으로 구축한 뒤,  
최종적으로 **Terraform modules + environment separation 구조**로 리팩토링한 프로젝트입니다.

- Networking, Secrets, Messaging, Redis Cache 계층 구성
- modules / environments 구조로 재사용 가능하게 정리
- Terraform 설계 판단과 모듈 체이닝 경험 정리

---

## Earlier Projects

- [face-tracking-robot-arm](https://github.com/JJong-03/face-tracking-robot-arm) — 얼굴 추적 촬영 보조 로봇팔, 졸업 캡스톤 4인 팀 팀장 · **정보기술대학장 장려상** · [Detail](https://kjw-cloud-portfolio.vercel.app/projects/face-tracking-robot-arm)
- [hearing-assist-headset-archive](https://github.com/JJong-03/hearing-assist-headset-archive) — 청각장애인 보조 헤드셋 프로토타입 · **2024 창업경진대회 수상** · [Detail](https://kjw-cloud-portfolio.vercel.app/projects/hearing-assist-headset-prototype)

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
  <a href="https://kjw-cloud-portfolio.vercel.app">
    <img src="https://img.shields.io/badge/Portfolio-326CE5?style=flat&logo=vercel&logoColor=white"/>
  </a>
</p>
