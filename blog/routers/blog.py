from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2
from ..repository import blog
from typing import List


router = APIRouter(
    tags=["Blogs"],
    prefix="/blog",
)
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowBlog])
def all_blog(db: Session= Depends(get_db),
             current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Moved to blog.py file under Repository folder
    # blogs = db.query(models.Blog).all()
    # return blogs
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session= Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Moved to blog.py file under Repository folder
    # new_blog = models.Blog(title= request.title, body= request.body, user_id= 1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db),
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Moved to blog.py file under Repository folder
    # blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID: {id} NOT FOUND")
    # blog.delete(synchronize_session=False)
    # db.commit()
    # return 'Done'
    return blog.destroy(id, db)


@router.put('/{id}', response_model=schemas.Blog ,status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Moved to blog.py file under Repository folder
    # blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID: {id} NOT FOUND")
    # blog.update(
    #     {models.Blog.title: request.title,
    #      models.Blog.body: request.body})
    # db.commit()
    # return request
    return blog.update(id, request, db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show_blog(id: int, db: Session= Depends(get_db),
              current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Moved to blog.py file under Repository folder
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Blog with ID: {id} Not Available")
    #     # response.status_code = status.HTTP_404_NOT_FOUND
    #     # return {'detail': f"Blog with ID: {id} Not Available"}
    # return blog
    return blog.show_one(id, db)