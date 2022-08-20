FROM python:3.10.6-slim-buster

COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8050
# CMD ["python3", "index.py"]
CMD ["gunicorn", "-b", "0.0.0.0:8050", "--reload", "index:server"]
