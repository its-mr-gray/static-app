import logging
import redis
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


# had to change file path from "static" to "src/static_app/static" bc the container didn't like it
static_file_path = "src/static_app/static"
app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=static_file_path),
    name="static",
)

r = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


@app.get("/api/message")
async def get_message():
    count = r.incr("click_count")
    logger.info("Click received, new count=%s", count)
    return {"message": "hello!", "count": count}


@app.get("/")
async def root():
    return FileResponse(static_file_path + "/index.html")
