from fastapi import FastAPI
import fastapi
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    publish: Optional[bool]


@app.get("/blog")
def index(limit, published:bool = True):
    if published:
        return {"data":f'{limit} publish blogs from db'}
    else:
        return {"data":'have no blog published'}

@app.get("/about")
def about():
    return {'data':'about the page!'}

@app.get("/blog/{id}")
def show(id:int):
    return {'blog':id}

@app.post("/blog")
def create_blog(blog:Blog ):
    return {'data':f'blog was created {blog.body}'}


