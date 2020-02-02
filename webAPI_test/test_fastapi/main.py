import aiohttp
from fastapi import FastAPI

app = FastAPI()

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

@app.get("/")
async def read_main():
    async with aiohttp.ClientSession() as session:
        a = await fetch(session, 'http://127.0.0.1')
    return {"msg": "Hello World"}
