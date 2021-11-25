from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import user, shift

router = APIRouter(
    prefix="/api/shift",
    tags=['Shift']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.Shift])
async def all_shift(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return shift.get_all(db)

# @router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
@router.get('/{id}', status_code=200, response_model=schemas.Shift)
async def show_shift(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return shift.show(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_shift(request: schemas.Shift, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return shift.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
async def destroy_shift(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return shift.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_shift(id:int , request: schemas.Shift, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return shift.update(id, request, db) 

