import aiohttp
from fastapi import FastAPI
from fastapi import FastAPI, Form

app = FastAPI()

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

@app.get("/")
async def read_main():
    async with aiohttp.ClientSession() as session:
        a = await fetch(session, 'http://127.0.0.1:8000/hi')
    return {"msg": "Hello World"}

@app.get("/hi")
async def hi():
    return {"msg": "Hi"}

@app.post("/api/post")
async def api_post(*, username: str = Form(...), password: str = Form(...)):
    return {"msg": "Hello POST"}

@app.post("/login/")
async def login(*, username: str = Form("username"), password: str = Form("password")):
    return {"username": username}
