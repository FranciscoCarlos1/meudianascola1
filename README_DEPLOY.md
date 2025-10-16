# Publicação no GitHub e Deploy no Railway

## 1) Subir para o seu repositório GitHub
Repositório indicado: `github.com/FranciscoCarlos1/meudianascola1`

```bash
# dentro da pasta meudianascola
git init
git branch -M main
git add .
git commit -m "MVP Meu Dia na Escola - backend+frontend+CI"
git remote add origin https://github.com/FranciscoCarlos1/meudianascola1.git
git push -u origin main
```

## 2) Criar projeto e serviços no Railway
- Crie 1 projeto no Railway (ex.: **meudianascola**).
- Adicione **dois serviços**:
  - **backend** (Python). Porta 8000. Variáveis: `SECRET_KEY`, `ADMIN_EMAIL`, `ADMIN_PASSWORD` (opcional).
  - **frontend** (Node static). Porta 8080. Variável de build: `VITE_API_URL=https://SUA_API.onrailway.app`
- Anote:
  - `RAILWAY_PROJECT_ID`
  - `RAILWAY_BACKEND_SERVICE`
  - `RAILWAY_FRONTEND_SERVICE`

## 3) Configurar *Secrets* no GitHub (repo Settings → Secrets and variables → Actions → New repository secret)
Crie estes *secrets*:
- `RAILWAY_TOKEN` — token obtido no Railway (Profile → Account → Railway Token).
- `RAILWAY_PROJECT_ID`
- `RAILWAY_BACKEND_SERVICE`
- `RAILWAY_FRONTEND_SERVICE`
- `VITE_API_URL` — URL pública da API (ex.: `https://meudianascola-api.up.railway.app`)

## 4) Pipeline automático
- Ao fazer *push* na branch `main`, os *workflows*:
  - `deploy-backend.yml` publica o backend
  - `deploy-frontend.yml` publica o frontend
- Aguarde a conclusão e acesse:
  - **Frontend** na URL do serviço web do Railway
  - **API** na URL do serviço backend (`/docs` para Swagger)

> Dica: se preferir, você pode fazer deploy pelo painel do Railway sem usar Actions. Os Dockerfiles já estão prontos.
