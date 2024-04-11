from fastapi import APIRouter , Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas
from models import User, get_password_hash
from database import  SessionLocal
import hashing

router = APIRouter(
    tags=["users"], prefix='/user'
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/add', response_model=schemas.Usershow)
def add_user(us: schemas.Users , db : Session = Depends(get_db)):
    user = User(email=us.email, password=get_password_hash(us.password), username=us.username )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get('/getall', response_model=schemas.Usershow)
def get_student(db : Session = Depends(get_db)):
    recs = db.query(User).all()
    return {"users":recs}

@router.get('/get/{id}', response_model=schemas.Usershow)
def get_student(id:int , db : Session = Depends(get_db)):
    recs = db.query(User).filter(User.id==id).first()
    if recs :
        return recs
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} not found" )


@router.delete('/delete/{id}',response_model=schemas.Usershow)
def get_student(id:int , db : Session = Depends(get_db)):
    try:
        db.query(User).filter(User.id == id).delete()
        db.commit()
        return "successfully delete"
    except Exception as e:
        raise Exception(e)



@router.put('/update/{id}')
def get_student(id:int ,stu:schemas.Users,  db : Session = Depends(get_db)):
    recs = db.query(User).filter(User.id==id).first()
    if recs :
        recs.username=stu.username
        recs.password = stu.password
        db.commit()
        return "updated"
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} not found" )
