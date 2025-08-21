#Imagem base em python
FROM python:3.13

#Confugura o diretorio base dentro do container 
WORKDIR /app

#Copia dependências e instala
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

#Copia o restante do projeto
COPY . .

#Expões a porta da aplicação
EXPOSE 8024

#Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8024"]