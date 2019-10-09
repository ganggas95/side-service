FROM python:3.7

ENV PYTHONUNBUFFERED 1

COPY . /side_service

WORKDIR /side_service

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system --dev

EXPOSE 9091

ENTRYPOINT ["./wait-for-it.sh"]
