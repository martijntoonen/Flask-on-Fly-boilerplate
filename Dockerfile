FROM python:3.10.9

RUN pip install pipenv
RUN apt-get update && apt-get install -y build-essential

WORKDIR /app
COPY Pipfile* ./
RUN pipenv install --system --deploy

COPY . .

EXPOSE 8080
CMD exec gunicorn --config /app/gunicorn.conf.py main:app