FROM python:3.11.0
# Set application working directory
WORKDIR /usr/src/app
# Install requirements
RUN pip3 install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --system --deploy
# Install application
COPY . ./
CMD python app.py