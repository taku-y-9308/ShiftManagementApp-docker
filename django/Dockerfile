FROM python:3.9.13

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt
COPY startup.sh /usr/src/app/startup.sh

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN mkdir -p /var/run/gunicorn
RUN chmod -R 755 .

CMD [ "./startup.sh" ]