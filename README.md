# AWS Cloud Resume Challenge ☁️🚀

![AWS](https://img.shields.io/badge/AWS-100000?style=for-the-badge&logo=amazon&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

## 🌐 Live Demo
👉 **[https://aminetraibi.com](https://aminetraibi.com)**

## 📖 The Story
I built a serverless resume website using AWS, Python, and automated CI/CD.
**Read the full technical deep-dive on my blog:**
👉 **[How I Built This: CI/CD, Python & Security Scares](https://dev.to/amine_traibi_ae1205ea170a/the-cloud-resume-challenge-cicd-python-and-surviving-a-security-scare-4af7)**

## 🏗 Architecture
*   **Frontend:** S3 + CloudFront (HTTPS)
*   **Backend:** API Gateway + Lambda (Python)
*   **Database:** DynamoDB (Atomic Counter)
*   **CI/CD:** GitHub Actions (Frontend & Backend pipelines)
*   **Infrastructure as Code:** Terraform / SAM

## 🧪 Tests
The Python backend includes unit tests using `unittest.mock` to simulate AWS services without hitting production endpoints.
