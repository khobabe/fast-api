from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message":"hello world, this is homepage"}

@app.get("/about")
async def about():
    return {"message":"hello world, this is about page"}