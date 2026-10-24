from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import redis

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


@app.get("/api/message")
async def get_message():
    count = r.incr("click_count")
    return {"message": "hello!", "count": count}


@app.get("/")
async def root():
    return FileResponse(static_file_path + "/index.html")
