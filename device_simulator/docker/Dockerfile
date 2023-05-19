FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . ../src

CMD [ "python", "-t" , "traffic", "-s", "4", "-i", "1"]