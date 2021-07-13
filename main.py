from fastapi import FastAPI
import fastapi


app = FastAPI()

@app.get("/")
def index():
    return {"data":{
        "name":"erik",
        "age":"22"
    }}

@app.get("/about")
def about():
    return {'data':'about the page!'}