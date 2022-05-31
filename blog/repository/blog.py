from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID: {id} NOT FOUND")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Done'


def update(id, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID: {id} NOT FOUND")
    blog.update(
        {models.Blog.title: request.title,
         models.Blog.body: request.body})
    db.commit()
    return request


def show_one(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with ID: {id} Not Available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with ID: {id} Not Available"}
    return blog