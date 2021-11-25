from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text

# Show All Staff
def get_all(db: Session):
    query = db.query(models.Staff).all()
    return query

# Show a Specific Staff
def show(id: int, db: Session):
    query = db.query(models.Staff).filter(models.Staff.id == id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Staff with ID {id} is not found')
    return query

# Create and Post a new Staff
def create(request: schemas.Staff, db: Session):
    new_staff = models.Staff(name=request.name, position=request.position, active=request.active, daily_salary=request.daily_salary, insurance=request.insurance, notes=request.notes )
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff

# Delete an Staff
def destroy(id: int, db: Session):
    staff = db.query(models.Staff).filter(models.Staff.id == id)
    if not staff.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The staff with id {id} is not found") 
    staff.delete(synchronize_session=False)
    db.commit()
    return "deleted!"

# Update an Staff
def update(id: int, request: schemas.Staff, db: Session):
    query = text("""UPDATE staff SET name=:name, position=:position, active=:active, daily_salary=:daily_salary, insurance=:insurance, notes=:notes WHERE id = :id""").params(name=request.name, position=request.position, active=request.active, daily_salary=request.daily_salary, insurance=request.insurance, notes=request.notes, id=id)
    result = db.execute(query)
    if not result:
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f'The staff with id {id} is not found')
    db.commit()
    return request
