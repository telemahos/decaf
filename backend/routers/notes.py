from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import notes, user

router = APIRouter(
    prefix="/api/notes",
    tags=['Notes']
)

get_db = database.get_db

@router.get('/', response_model = List[schemas.NotesOut])
async def all_notes(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return notes.get_all(db)

@router.post('/', response_model = schemas.NotesOut, status_code=status.HTTP_201_CREATED)
async def create_note(request: schemas.NotesIn, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return notes.create(request, db)