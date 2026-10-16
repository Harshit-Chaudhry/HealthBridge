from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello, World"}

@app.get("/health")
def health():
    return {"message": "its working"}

@app.post("/post")
def post():
    return {"message":"posssting"}