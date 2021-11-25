from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text

# Show All Incomes
def get_all(db: Session):
    suppliers = db.query(models.Suppliers).all()
    return suppliers

# Show a Specific Supplier
def show(id: int, db: Session):
    suppliers = db.query(models.Suppliers).filter(models.Suppliers.id == id).first()
    if not suppliers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The suppliers with ID {id} is not found')
    return suppliers

# # Create and Post a new Income
def create(request: schemas.Suppliers, db: Session):
    new_suppliers = models.Suppliers(company_name=request.company_name, responsible=request.responsible, address=request.address, telephone=request.telephone, email=request.email, payment_way=request.payment_way, notes=request.notes )
    db.add(new_suppliers)
    db.commit()
    db.refresh(new_suppliers)
    return new_suppliers

# # Delete an Income
def destroy(id: int, db: Session):
    suppliers = db.query(models.Suppliers).filter(models.Suppliers.id == id)
    if not suppliers.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The suppliers with id {id} is not found") 
    suppliers.delete(synchronize_session=False)
    db.commit()
    return "deleted!"

# # Update an Income
def update(id: int, request: schemas.Suppliers, db: Session):
    query = text("""UPDATE suppliers SET company_name=:company_name, responsible=:responsible, address=:address, telephone=:telephone, email=:email, payment_way=:payment_way, notes=:notes WHERE id = :id""").params(company_name=request.company_name, responsible=request.responsible, address=request.address, telephone=request.telephone, email=request.email, payment_way=request.payment_way, notes=request.notes, id=id)
    result = db.execute(query)
    if not result:
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f'The suppliers with id {id} is not found')
    db.commit()
    return request
