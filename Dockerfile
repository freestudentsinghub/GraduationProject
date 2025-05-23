FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SECRET_KEY="django-insecure-qa&(9423y2ymk_ty5kgp#&=_*7dnx=@h3nm34h$d1*9@lm)ysn"

RUN mkdir -p /app/media

EXPOSE 8000

# CMD ["poetry", "run", "sh", "-c", "python manage.py migrate && python manage.py csu && python manage.py runserver 0.0.0.0:8000"]