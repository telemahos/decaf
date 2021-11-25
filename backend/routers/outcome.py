from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import user, staff, suppliers, outcome

router = APIRouter(
    prefix="/api/outcome",
    tags=['Outcome']
)

get_db = database.get_db

# Get all Outcome
@router.get('/', response_model=List[schemas.Outcome])
async def all_outcome(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return outcome.get_all(db)

# Show a specific Outcome
@router.get('/{id}', status_code=200, response_model=schemas.Outcome)
async def show_outcome(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return outcome.show(id, db)

# Create a new Outcome
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_outcome(request: schemas.Outcome, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return outcome.create(request, db)

# Delete a Outcome
@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
async def destroy_outcome(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return outcome.destroy(id, db)

# Update a Outcome
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_outcome(id:int , request: schemas.Outcome, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return outcome.update(id, request, db) 