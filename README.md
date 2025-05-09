# 🚀 FastAPI CRM System

![FastAPI](https://img.shields.io/badge/FastAPI-powered-green?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-ready-blue?style=for-the-badge&logo=docker)
![Python](https://img.shields.io/badge/Python-3.12+-yellow?style=for-the-badge&logo=python)
![Next](https://img.shields.io/badge/Next.js-white?style=for-the-badge&logo=next)

## 🧾 О проекте

**FastAPI CRM System** — CRM-система для управления торговыми процессами.  
Работает на базе **FastAPI**, обеспечивая высокую производительность, асинхронность и удобный REST API с автоматической документацией.
---

- 📄 Доступ к интерактивной документации по адресу:  
  👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Для разработки

### 🔑 Генерация секретного ключа

```bash
python -c "import secrets; print(secrets.token_hex())"
```

<p>Dockerfile</p>

```bash
docker build . -t crm
docker run -it -p 8000:8000 crm
```
<p>docker-compose</p>

```bash
docker-compose up --build
```