FROM            python:3.10
COPY            ./requirements.txt /webapp/requirements.txt
WORKDIR         /webapp
RUN             pip install -r requirements.txt
COPY            main.py /webapp

EXPOSE          8000
ENTRYPOINT      [ "uvicorn" ]
CMD             ["--host", "0.0.0.0", "main:app"]
