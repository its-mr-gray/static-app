FROM python:3.14

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src

RUN ls src/static_app/static
CMD ["fastapi", "run", "src/static_app/main.py", "--port", "80"]
