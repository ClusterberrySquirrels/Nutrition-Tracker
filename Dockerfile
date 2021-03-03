FROM python:3

MAINTAINER Noah Laratta "noahlaratta@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "__init__.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG true

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
EXPOSE 5000

CMD flask run --host=0.0.0.0
