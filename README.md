# Meu Dia na Escola (MVP completo)

Projeto full-stack mínimo (FastAPI + SQLite + Vue 3 + Vite) para cadastro de alunos, turmas, frequência e notas.

## Como rodar localmente

### Backend
```bash
cd backend
cp .env.example .env   # (opcional) ajuste o SECRET_KEY
./run.sh               # ou: python -m pip install -r requirements.txt && uvicorn app.main:app --reload
# API: http://localhost:8000/docs
```

Usuário inicial: **admin@escola.local** / **admin123**

### Frontend
```bash
cd frontend
npm i
npm run dev
# Web: http://localhost:5173
```

Crie login na tela com o usuário padrão acima.

## Deploy (Railway - sugestão simples)

1. Crie dois projetos no Railway: `api` e `web`.
2. API:
   - Deploy da pasta `backend` (Python).
   - Defina `SECRET_KEY`, `ADMIN_EMAIL`, `ADMIN_PASSWORD` nas variáveis.
   - Defina o `PORT` (Railway define automaticamente); configure o start command: `uvicorn app.main:app --host 0.0.0.0 --port ${PORT}`.
   - A base SQLite será um arquivo no container; para produção, considere PostgreSQL.
3. Web:
   - Deploy da pasta `frontend` (Node) com build.
   - Comando: `npm i && npm run build && npm i -g serve && serve -s dist -l ${PORT}`
   - Variável em build: `VITE_API_URL=https://SEU_BACKEND.onrender.com` (ou Railway URL da API).

## Endpoints principais

- `POST /auth/login` (OAuth2 - form `username`/`password`)
- `GET/POST/PUT/DELETE /students`
- `GET/POST/PUT/DELETE /classes`
- `GET/POST /attendance`
- `GET /grades/{student_id}`
- `POST /grades`

## Observações
- Banco padrão: SQLite local (`backend/app/database.py`).
- JWT & CORS prontos.
- Estrutura pensada para evoluir: adicionar usuários professores, relatórios, exportação CSV, etc.
