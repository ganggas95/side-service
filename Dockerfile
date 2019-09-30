FROM python:3.7

ENV PYTHONUNBUFFERED 1

COPY . /users_service

WORKDIR /users_service

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system --dev

ENTRYPOINT ["python"]

EXPOSE 5000

CMD ["manage.py", "runserver"]
