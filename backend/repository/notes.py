from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text
from sqlalchemy import desc

def get_all(db: Session, limit: int = 3, offset: int = 0):
    print("HALLO KSOTAS")
    notes = db.query(models.Notes).order_by(desc('id')).offset(offset).limit(limit).all()
    print("notes: ", notes)
    return notes

def create(request: schemas.NotesIn, db: Session):
    new_note = models.Notes(date=request.date, title=request.title, body=request.body, tags=request.tags, active=request.active, author_id = 1)
    if not new_note:
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail=f'The note with id {id} is not found')
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    print("new_note: ", new_note)
    return new_note