FROM python:3.10.9-slim


ENV YOUR_ENV=production

WORKDIR /app


RUN pip install 'poetry==1.2.2'

COPY app.py twitter_checker.py poetry.lock pyproject.toml /app/
COPY website /app/website

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --only main --no-interaction --no-ansi