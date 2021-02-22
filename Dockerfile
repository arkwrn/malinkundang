FROM python:3.7.2

ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt

EXPOSE 1337

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "1337"]
