from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text

# Show All FixedCost
def get_all(db: Session):
    query = db.query(models.FixedCost).all()
    return query

# Show a Specific FixedCost
def show(id: int, db: Session):
    query = db.query(models.FixedCost).filter(models.FixedCost.id == id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Staff with ID {id} is not found')
    return query

# Create and Post a new FixedCost
def create(request: schemas.FixedCost, db: Session):
    new_fixedCost = models.FixedCost(name=request.name )
    db.add(new_fixedCost)
    db.commit()
    db.refresh(new_fixedCost)
    return new_fixedCost

# Delete an Staff
def destroy(id: int, db: Session):
    fixedCost = db.query(models.FixedCost).filter(models.FixedCost.id == id)
    if not fixedCost.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The staff with id {id} is not found") 
    fixedCost.delete(synchronize_session=False)
    db.commit()
    return "deleted!"

# Update an FixedCost
def update(id: int, request: schemas.FixedCost, db: Session):
    query = text("""UPDATE fixed_cost SET name=:name WHERE id = :id""").params(name=request.name, position=request.position, active=request.active, daily_salary=request.daily_salary, insurance=request.insurance, notes=request.notes, id=id)
    result = db.execute(query)
    if not result:
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f'The staff with id {id} is not found')
    db.commit()
    return request
