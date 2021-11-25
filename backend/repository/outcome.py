from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text

# Show All Outcome
def get_all(db: Session):
    query = db.query(models.Outcome).all()
    return query

# Show a Specific Outcome
def show(id: int, db: Session):
    query = db.query(models.Outcome).filter(models.Outcome.id == id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Outcome with ID {id} is not found')
    return query

# Create and Post a new Outcome
def create(request: schemas.Outcome, db: Session):
    new_outcome = models.Outcome(date=request.date, description=request.description, invoice_number=request.invoice_number, cost=request.cost, extra_cost=request.extra_cost, tax_perc=request.tax_perc , tax_perc2=request.tax_perc2, supplier_id=request.supplier_id, fixed_cost_id=request.fixed_cost_id, staff_id=request.staff_id, is_variable_cost=request.is_variable_cost, is_fix_cost=request.is_fix_cost, is_purchase_cost=request.is_purchase_cost, is_salary_cost=request.is_salary_cost, is_insurance_cost=request.is_insurance_cost, is_misc_cost=request.is_misc_cost, payment_way=request.payment_way, is_paid=request.is_paid, outcome_notes=request.outcome_notes)
    db.add(new_outcome)
    db.commit()
    db.refresh(new_outcome)
    return new_outcome

# date=request.date, description=request.description, invoice_number=request.invoice_number, cost=request.cost, extra_cost=request.extra_cost, tax_perc=request.tax_perc, tax_perc2=request.tax_perc2, supplier_id=request.supplier_id, staff_id=request.staff_id, is_variable_cost=request.is_variable_cost, is_fix_cost=request.is_fix_cost, is_purchase_cost=request.is_purchase_cost, is_salary_cost=request.is_salary_cost, is_insurance_cost=request.is_insurance_cost, is_misc_cost=request.is_misc_cost, payment_way=request.payment_way, is_paid=request.is_paid, outcome_notes=request.outcome_notes 

# Delete an Outcome
def destroy(id: int, db: Session):
    outcome = db.query(models.Outcome).filter(models.Outcome.id == id)
    if not outcome.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Outcome with id {id} is not found") 
    outcome.delete(synchronize_session=False)
    db.commit()
    return "deleted!"

# Update an Outcome
def update(id: int, request: schemas.Outcome, db: Session):
    query = text("""UPDATE outcome SET date=:date, description=:description, invoice_number=:invoice_number, cost=:cost, extra_cost=:extra_cost, tax_perc=:tax_perc, tax_perc2=:tax_perc2, supplier_id=:supplier_id, fixed_cost_id=:fixed_cost_id, staff_id=:staff_id, is_variable_cost=:is_variable_cost, is_fix_cost=:is_fix_cost, is_purchase_cost=:is_purchase_cost, is_salary_cost=:is_salary_cost, is_insurance_cost=:is_insurance_cost, is_misc_cost=:is_misc_cost, payment_way=:payment_way, is_paid=:is_paid, notes=:notes WHERE id = :id""").params(date=request.date, description=request.description, invoice_number=request.invoice_number, cost=request.cost, extra_cost=request.extra_cost, tax_perc=request.tax_perc, tax_perc2=request.tax_perc2, supplier_id=request.supplier_id, staff_id=request.staff_id, fixed_cost_id=request.fixed_cost_id, is_variable_cost=request.is_variable_cost, is_fix_cost=request.is_fix_cost, is_purchase_cost=request.is_purchase_cost, is_salary_cost=request.is_salary_cost, is_insurance_cost=request.is_insurance_cost, is_misc_cost=request.is_misc_cost, payment_way=request.payment_way, is_paid=request.is_paid, notes=request.notes, id=id)
    result = db.execute(query)
    if not result:
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f'The outcome with id {id} is not found')
    db.commit()
    return request
