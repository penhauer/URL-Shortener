FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
COPY ./entrypoint.sh .
RUN chmod +x entrypoint.sh

EXPOSE 80

CMD ["./entrypoint.sh"]
