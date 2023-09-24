FROM python:3.11.5-alpine3.18

WORKDIR /code

COPY requirements.txt /code/

RUN pip3 install -r requirements.txt

COPY . /code

ENTRYPOINT ["python3"]

CMD ["app.py"]