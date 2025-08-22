# #Imagem base em python
# FROM python:3.13

# #Confugura o diretorio base dentro do container 
# WORKDIR /app

# #Copia dependências e instala
# COPY requirements.txt . 
# RUN pip install --no-cache-dir -r requirements.txt

# #Copia o restante do projeto
# COPY . .

# #Expões a porta da aplicação
# EXPOSE 8034

# #Comando para rodar o servidor
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8034"]


# Etapa 1: base
FROM python:3.12-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Instala dependências do sistema necessárias (ajuste se precisar de libs extras)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Cria usuário não-root
RUN useradd -m appuser

WORKDIR /app

# Copia e instala dependências primeiro (melhor cache)
COPY requirements.txt /app/
RUN python -m venv /opt/venv && /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt

# Copia o código
COPY app /app/app

# Porta padrão do Uvicorn
EXPOSE 8000

# Garante que o venv esteja no PATH
ENV PATH="/opt/venv/bin:$PATH"

# Troca para usuário não-root
USER appuser

# Comando padrão (produção, sem reload)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]