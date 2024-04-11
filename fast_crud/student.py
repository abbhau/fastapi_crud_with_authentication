from fastapi import APIRouter , Depends, HTTPException, status
from sqlalchemy.orm import Session
from oauth2 import get_current_user
import schemas
from models import User, Student
from database import  SessionLocal

router = APIRouter(
    tags=["students"], prefix='/student'
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/add')
def add_student(stu: schemas.Students , db : Session = Depends(get_db), get_current_user:schemas.Users=Depends(get_current_user)):
    stu = Student(roll=stu.roll, name= stu.name, marks=stu.marks, user_id=stu.user_id)
    db.add(stu)
    db.commit()
    db.refresh(stu)
    return stu

@router.get('/get')
def get_student(db : Session = Depends(get_db)):
    recs = db.query(Student).all()
    return recs

@router.get('/get/{id}')
def get_student(id:int , db : Session = Depends(get_db)):
    recs = db.query(Student).filter(Student.id==id).first()
    if recs :
        return recs
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} not found" )


@router.delete('/delete/{id}')
def get_student(id:int , db : Session = Depends(get_db)):
    try:
        db.query(Student).filter(Student.id == id).delete()
        db.commit()
        return "successfully delete"
    except Exception as e:
        raise Exception(e)



@router.put('/update/{id}')
def get_student(id:int ,stu:schemas.Students,  db : Session = Depends(get_db)):
    recs = db.query(Student).filter(Student.id==id).first()
    if recs :
        recs.name=stu.name
        recs.marks=stu.marks
        recs.roll = stu.roll
        db.commit()
        return "updated"
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} not found" )



