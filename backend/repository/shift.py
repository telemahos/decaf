from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text

# Show All Shift
def get_all(db: Session):
    query = db.query(models.Shift).all()
    return query

# Show a Specific Shift
def show(id: int, db: Session):
    query = db.query(models.Shift).filter(models.Shift.id == id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Shift with ID {id} is not found')
    return query

# Create and Post a new Shift
def create(request: schemas.Shift, db: Session):
    new_shift = models.Shift(service_id_1=request.service_id_1, barman_id_1=request.barman_id_1, service_id_2=request.service_id_2, barman_id_2=request.barman_id_2 )
    db.add(new_shift)
    db.commit()
    db.refresh(new_shift)
    return new_shift

# Delete an Shift
def destroy(id: int, db: Session):
    shift = db.query(models.Shift).filter(models.Shift.id == id)
    if not shift.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Shift with id {id} is not found") 
    shift.delete(synchronize_session=False)
    db.commit()
    return "deleted!"

# Update an Shift
def update(id: int, request: schemas.Shift, db: Session):
    query = text("""UPDATE shift SET service_id_1=:service_id_1, barman_id_1=:barman_id_1, service_id_2=:service_id_2, barman_id_2=:barman_id_2 WHERE id = :id""").params(service_id_1=request.service_id_1, barman_id_1=request.barman_id_1, service_id_2=request.service_id_2, barman_id_2=request.barman_id_2, id=id)
    result = db.execute(query)
    if not result:
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f'The Shift with id {id} is not found')
    db.commit()
    return request
