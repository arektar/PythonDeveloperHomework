FROM python:3.10-slim-buster

WORKDIR /usr/src/PDH

COPY . .
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000

ENTRYPOINT [ "python", "-u", "./main.py" ]