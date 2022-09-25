FROM tiangolo/uvicorn-gunicorn:python3.9-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

EXPOSE 8001

WORKDIR /fast_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8001", "main:app"]
