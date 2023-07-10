FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

STOPSIGNAL SIGINT

CMD [ "python", "./app.py" ]