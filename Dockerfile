
FROM python:3.8-slim-buster

WORKDIR /text-analyser

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN export FLASK_APP=wsgi.py

ENV GOOGLE_APPLICATION_CREDENTIALS sa.json
EXPOSE 8000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000"]