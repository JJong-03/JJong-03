# 김종원 | 클라우드 인프라 / DevOps 신입

Terraform으로 AWS와 GCP 인프라를 만들고 Kubernetes로 서비스를 배포했습니다.
요청이 실패하면 막힌 구간을 찾아 고치고, 고친 뒤 무엇을 확인했는지 기록합니다.

[웹 포트폴리오](https://kjw-cloud-portfolio.vercel.app) | [이력서](https://kjw-cloud-portfolio.vercel.app/resume) | jowon7602@gmail.com

## 대표 프로젝트

| 프로젝트 | 맡은 일 | 해결한 문제와 확인 |
|---|---|---|
| [Aegis-Pi Risk Twin](https://github.com/aegis-pi/dashboard_vpc)<br>2인 팀, MSP 최종 프로젝트 최우수팀(팀) | 데이터/대시보드 VPC Terraform, FastAPI 백엔드, React 관제 화면, DynamoDB Streams와 Redis 실시간 알림, Bedrock AI 채팅 | 이력 조회 504를 막은 임시 조치가 지나간 위험 신호를 지운 것을 찾아, 팀원과 기간별 조회로 나눠 해결. 이력 조회 테스트 38개 재실행 통과(응답 시간은 재지 않음) |
| [Kubernetes 백테스트 플랫폼](https://github.com/JJong-03/stock-backtest-platform)<br>개인, MSP 개인 프로젝트 우수상 | 요청마다 Kubernetes Job 실행, run_id 추적, GitHub Actions와 Argo CD, Prometheus와 Grafana | 로컬 kind 1노드 부하 측정으로 병목(결과 조회)을 찾고, 웹 워커 2개, CPU 1코어, 메모리 1Gi 구성에서 처리량이 분당 27.7건에서 43.7건으로 늘어남(+58%, 구성별 1회 측정) |
| [AWS Multi-VPC 인프라](https://github.com/JJong-03/aws-terraform-multi-vpc)<br>개인 PoC | VPC 3개로 사용자, 관리자, 서비스 경로 분리. CloudFront, WAF, ALB, EKS, Aurora, OpenVPN | EC2 Nginx에서 EKS로 가는 504를 보안 그룹과 호출 주소, 두 원인으로 나눠 복구. 배포 뒤 8단계 점검 |
| [GCP GKE GitOps](https://github.com/JJong-03/gcp-gke-gitops-pipeline)<br>개인 실습 | Terraform, GitHub Actions와 WIF(키 파일 없음), Artifact Registry, Argo CD | 노드 2대에서 멈춘 롤아웃을 교체 순서(maxSurge 0)로 끝내고 Pod 2/2, HTTP 200 확인 |
| [LawMainRoad](https://github.com/2026-moel-datacontest-core/law_main_road_main)<br>2인 팀 | 노동 분쟁 사후 대응(After) 기능, GCP 이전(Cloud Run, Cloud SQL, WIF 배포와 롤백) | 법령 1,722개 조각에서 근거와 함께 답하는 흐름. 60문항 자체 평가 충족 44, 부분 충족 16, 실패 0(2026-04-20) |
| [Terraform 모듈 리팩터링](https://github.com/JJong-03/aws-terraform-deepdive)<br>교육 미션 선택 심화 | 네트워크, 비밀값, 메시징, 캐시 4개 모듈과 dev/prod 환경 분리 | 모듈 출력값을 바로 넘겨 상태 파일 참조를 없애고, 환경별 plan으로 확인(prod는 비용 때문에 적용하지 않음) |

시연용 클라우드 자원은 확인 뒤 정리했습니다. 실행 화면과 검증 기록은 각 저장소와 웹 포트폴리오에 있습니다.

## 프로젝트에서 직접 쓴 기술

- 클라우드: AWS (VPC, EKS, ECS Fargate, ALB, CloudFront, DynamoDB, Lambda, Cognito, Bedrock), GCP (GKE, Cloud Run, Cloud SQL)
- IaC와 배포: Terraform (모듈, dev/prod 분리), GitHub Actions, Argo CD, WIF
- 실행과 관측: Linux, Docker, Kubernetes, Prometheus, Grafana
- 개발: Python (FastAPI, Flask), React, MySQL, Redis

## 그 밖의 경험

- [얼굴 추적 로봇팔](https://github.com/JJong-03/face-tracking-robot-arm): 졸업작품 4인 팀 팀장, 정보기술대학장 장려상(팀)
- [청각 보조 헤드셋](https://github.com/JJong-03/hearing-assist-headset-archive): 창업경진대회 5인 팀, 학장상(팀)
- 인천대학교 임베디드시스템공학과 졸업(2026.08), 메가존클라우드 MSP 솔루션 아키텍트 양성과정 8기 수료
