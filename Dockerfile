FROM python:3.9
MAINTAINER chiragsanghvi10@gmail.com
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 7003
CMD ["gunicorn","--bind","0.0.0.0:7003","main:app","--timeout=60"]
