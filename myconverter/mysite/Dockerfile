FROM python:3.9
EXPOSE 8000
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt --no-cache-dir
COPY . /code/
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]

#http://0.0.0.0:8000/filmwork/
