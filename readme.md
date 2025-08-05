# 🚀 API FastAPI: Sistema de Gestión de Tareas

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql)

API moderna para gestión de tareas con autenticación JWT, perfecta para aprender FastAPI o usar como base para tus proyectos.

## 🔥 Características Principales
- ✅ Autenticación con JWT (tokens seguros)
- 📝 CRUD completo de tareas
- 🛡️ Protección de endpoints con roles
- 🐘 Compatible con PostgreSQL y SQLite
- 📚 Documentación automática (Swagger/Redoc)

## 📦 Requisitos
- Python 3.9+
- Pipenv o pip
- PostgreSQL (opcional)

## 🛠️ Instalación Local
```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/mi-api-fastapi.git
cd mi-api-fastapi

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno (crea un archivo .env)
echo "SECRET_KEY=mi_clave_super_secreta" > .env
echo "DATABASE_URL=sqlite:///./local.db" >> .env

# Ejecutar
uvicorn main:app --reload