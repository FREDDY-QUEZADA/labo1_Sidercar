FROM python:3.9
WORKDIR /app
COPY requeriments.txt .
RUN pip install -r requeriments.txt
COPY app.py .

CMD ["python", "app.py"]
