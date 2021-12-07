FROM python:slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python" , "manage.py", "runserver" , "0.0.0.0:8000"]

# docker build --tag python-drf .
# docker run --publish 8000:8000 python-drf