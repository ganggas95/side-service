FROM python:3.7

ENV PYTHONUNBUFFERED 1

COPY . /side_service

WORKDIR /side_service

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9091

# ENTRYPOINT ["python", "manage.py", "runserver"]
