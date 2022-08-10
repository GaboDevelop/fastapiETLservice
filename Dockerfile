# Pull base image
FROM python:3.8
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code/
# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv lock && pipenv install --system --dev
COPY . /code/
EXPOSE 8000
#RUN ./prestart.sh
CMD ["python","-m", "app.main"]