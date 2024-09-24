# Use uma imagem base do Python
FROM python:3.12.6

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta em que o servidor irá rodar
EXPOSE 5050

# Comando para rodar a aplicação
CMD ["python3", "-u", "server.py"]