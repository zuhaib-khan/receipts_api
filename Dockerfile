FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

EXPOSE 5000

CMD ["flask", "--app=api/app.py",  "run", "--host=0.0.0.0", "--port=5000"]

