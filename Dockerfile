FROM python:3.5-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 3000
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
LABEL maintainer="Team DevOps"
COPY . .
CMD ["flask", "run"]
