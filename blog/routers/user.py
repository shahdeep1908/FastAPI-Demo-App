from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas
from ..repository import user

router = APIRouter(
    tags=["Users"],
    prefix="/user"
)
get_db = database.get_db


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # Moved to user.py File in Repository Folder
    # Moved to hashing.py File
    # hashed_password = pwd_cxt.hash(request.password)
    # new_user =  models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user
    return user.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session= Depends(get_db)):
    # Moved to user.py File in Repository Folder
    # user = db.query(models.User).filter(models.User.id == id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID: {id} NOT FOUND")
    # return user
    return user.show_one(id, db)