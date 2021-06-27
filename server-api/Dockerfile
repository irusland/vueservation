FROM python:3.9

COPY requirements.txt app/requirements.txt
WORKDIR /app
RUN python3 -m pip install -r requirements.txt
COPY secret_tokens ./secret_tokens
COPY app.py .
COPY handlers ./handlers
COPY database ./database
COPY env ./env
COPY pictures ./pictures

EXPOSE 8000
CMD python app.py
