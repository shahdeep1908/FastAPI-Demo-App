from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI()


@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # ONLY GET LIMITS OF BLOGS.
    if published:
        return {'data': f'{limit} Published Blogs List Fetched'}
    else:
        return {'data': f'{limit} Blogs List Fetched'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'All Unpublished Blogs'}


@app.get("/blog/{id}")
def show(id: int):
    # FETCH BLOG WITH ID
    return {'data': id}


@app.get("/blog/{id}/comments")
def comments(id, limit=10):
    # FETCH COMMENTS OF BLOGS WITH ID
    return {'data': {"1", "2"}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'New Blog Created with title as {blog.title}'}


# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=5000)