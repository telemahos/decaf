from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import user, suppliers

router = APIRouter(
    prefix="/api/suppliers",
    tags=['Suppliers']
)

get_db = database.get_db

# Get all Suppliers
@router.get('/', response_model=List[schemas.Suppliers])
async def all_suppliers(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return suppliers.get_all(db)

# Show a specific Supplier
@router.get('/{id}', status_code=200, response_model=schemas.Suppliers)
async def show_suppliers(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return suppliers.show(id, db)

# Create a new Supplier
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_suppliers(request: schemas.Suppliers, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return suppliers.create(request, db)

# Delete a Supplier
@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
async def destroy_suppliers(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return suppliers.destroy(id, db)

# Update a Supplier
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_suppliers(id:int , request: schemas.Suppliers, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return suppliers.update(id, request, db) 