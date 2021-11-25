from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import user, fixedCost

router = APIRouter(
    prefix="/api/fixedcost",
    tags=['Fixed Cost']
)

get_db = database.get_db

# Get all Fixed Cost
@router.get('/', response_model=List[schemas.FixedCost])
async def all_fixedCost(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return fixedCost.get_all(db)

# Show a specific Fixed Cost
@router.get('/{id}', status_code=200, response_model=schemas.FixedCost)
async def show_fixedCost(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return fixedCost.show(id, db)

# Create a new Fixed Cost
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_fixedCost(request: schemas.FixedCost, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return fixedCost.create(request, db)

# Delete a Fixed Cost
@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
async def destroy_fixedCost(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return fixedCost.destroy(id, db)

# Update a Fixed Cost
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_fixedCost(id:int , request: schemas.FixedCost, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return fixedCost.update(id, request, db) 