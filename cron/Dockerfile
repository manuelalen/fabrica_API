FROM python:3.10
RUN apt-get update && apt-get install -y cron
WORKDIR /scripts
COPY script_insert.py .
COPY script_sync.py .
COPY crontab.txt .
RUN pip install mysql-connector-python requests
RUN crontab crontab.txt
CMD cron -f
