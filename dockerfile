FROM pypy:latest

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
