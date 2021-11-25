from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import user, staff

router = APIRouter(
    prefix="/api/staff",
    tags=['Staff']
)

get_db = database.get_db

# Get all Staff
@router.get('/', response_model=List[schemas.Staff])
async def all_staff(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return staff.get_all(db)

# Show a specific Staff
@router.get('/{id}', status_code=200, response_model=schemas.Staff)
async def show_staff(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return staff.show(id, db)

# Create a new Staff
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_staff(request: schemas.Staff, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return staff.create(request, db)

# Delete a Staff
@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
async def destroy_staff(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return staff.destroy(id, db)

# Update a Staff
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_staff(id:int , request: schemas.Staff, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return staff.update(id, request, db) 