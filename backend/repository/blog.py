from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text
from sqlalchemy import desc

def get_all(db: Session, limit: int = 3, offset: int = 0):
    blogs = db.query(models.Blog).order_by(desc('id')).offset(offset).limit(limit).all()
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(date=request.date, title=request.title, body=request.body, tags=request.tags, active=request.active, author_id=1)
    if not new_blog:
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail=f'The post with id {id} is not found')
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id {id} is not found") 
    blog.delete(synchronize_session=False)
    db.commit()
    return "deleted!"

def update(id: int, request: schemas.Blog, db: Session):
    query = text("""UPDATE blogs SET date=:date, title=:title, body=:body, tags=:tags, active=:active  WHERE id = :id""").params(date=request.date, title=request.title, body=request.body, tags= request.tags, active= request.active, id=id)
    result = db.execute(query)
    if not result:
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f'The post with id {id} is not found')
    db.commit()
    return request

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Blog with ID {id} is not found')
    return blog