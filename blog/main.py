from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication

app = FastAPI()
models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

# Moved To Routers Directory in Blog.py File
# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=["blogs"])
# def create(request: schemas.Blog, db: Session= Depends(get_db)):
#     new_blog = models.Blog(title= request.title, body= request.body, user_id= 1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# Moved To Routers Directory in Blog.py File
# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
# def destroy(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID: {id} NOT FOUND")
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'Done'


# Moved To Routers Directory in Blog.py File
# @app.put('/blog/{id}', response_model=schemas.Blog ,status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
# def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID: {id} NOT FOUND")
#     blog.update(
#         {models.Blog.title: request.title,
#          models.Blog.body: request.body})
#     db.commit()
#     return request


# Moved To Routers Directory in Blog.py File
# @app.get("/blog", response_model=List[schemas.ShowBlog], tags=["blogs"])
# def all_blog(db: Session= Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# Moved To Routers Directory in Blog.py File
# @app.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog, tags=["blogs"])
# def show_blog(id, response: Response, db: Session= Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with ID: {id} Not Available")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail': f"Blog with ID: {id} Not Available"}
#     return blog


# Moved to hashing.py File
# pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Moved To Routers Directory in User.py File
# @app.post("/user", response_model=schemas.ShowUser, tags=["users"])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     # Moved to hashing.py File
#     # hashed_password = pwd_cxt.hash(request.password)
#     new_user =  models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# Moved To Routers Directory in User.py File
# @app.get("/user/{id}", response_model=schemas.ShowUser, tags=["users"])
# def get_user(id: int, db: Session= Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID: {id} NOT FOUND")
#     return user