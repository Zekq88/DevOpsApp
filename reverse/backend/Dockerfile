FROM python:3.13

WORKDIR /app

COPY req.txt .
RUN pip install -r req.txt

COPY . .

CMD ["python", "app.py"]