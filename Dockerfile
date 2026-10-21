FROM python:3.14-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./

COPY src/ ./src/

COPY README.md ./

RUN uv sync --frozen

CMD ["uv", "run", "fastapi", "run", "src/static_app/main.py", "--host", "0.0.0.0", "--port", "8000"]
