from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

static_file_path = "static"
app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=static_file_path),
    name="static",
)


@app.get("/api/message")
async def get_message():
    return {"message": "hello!"}


@app.get("/")
async def root():
    return FileResponse(static_file_path + "/index.html")
