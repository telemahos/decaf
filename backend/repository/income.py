import re
import json
from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text
from sqlalchemy import desc
# from fastapi_pagination import Page, pagination_params, page_size


# Show All Incomes ##.order_by(desc('date'))
def get_all(db: Session, limit: int = 10, offset: int = 0 ):
    income = db.query(models.Income).offset(offset).limit(limit).all()
    # income = db.query(models.Income).filter(models.Income.date >= "2021-09-01", models.Income.date <= "2021-09-31").all()
    return income

# Show a Specific Income by date year: str, month: str,
def show_by_date(year:str, month:str, db: Session, limit: int = 10, offset: int = 0 ):
    # print(" TEST.....show_by_date22")
    income = db.query(models.Income).filter(models.Income.date >= f'{year}-{month}-01', models.Income.date <= f'{year}-{month}-31').all()
    return income

# Show a Specific Income by id
def show(id: int, db: Session):
    income = db.query(models.Income).filter(models.Income.id == id).first()
    if not income:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Income with ID {id} is not found')
    return income

# Create and Post a new Income
def create(request: schemas.Income, db: Session):
    # print("HALLO TEST..............")
    new_income = models.Income(date=request.date, service_income_1 = request.service_income_1, service_income_2 = request.service_income_2, bar_income_1=request.bar_income_1, bar_income_2=request.bar_income_2, pos=request.pos, z_count=request.z_count, vat=request.vat, waitress_1=request.waitress_1, waitress_2=request.waitress_2, barman_1=request.barman_1, barman_2=request.barman_2, notes=request.notes, shift_id=request.shift_id )
    db.add(new_income)
    db.commit()
    db.refresh(new_income)
    # print("HALLO TEST..............222222222")
    return new_income

# Update an Income
def update(id: int, request: schemas.Income, db: Session):
    query = text("""UPDATE income SET date=:date, service_income_1=:service_income_1, service_income_2=:service_income_2, bar_income_1=:bar_income_1, bar_income_2=:bar_income_2, pos=:pos, z_count=:z_count, vat=:vat, waitress_1=:waitress_1, waitress_2=:waitress_2, barman_1=:barman_1, barman_2=:barman_2, notes=:notes, shift_id=:shift_id WHERE id = :id""").params( date=request.date, service_income_1 = request.service_income_1, service_income_2 = request.service_income_2, bar_income_1=request.bar_income_1, bar_income_2=request.bar_income_2, pos=request.pos, z_count=request.z_count, vat=request.vat, waitress_1=request.waitress_1, waitress_2=request.waitress_2, barman_1=request.barman_1, barman_2=request.barman_2, notes=request.notes, shift_id=request.shift_id , id=id)
    result = db.execute(query)
    if not result:
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f'The income with id {id} is not found')
    db.commit()
    return request

# Delete an Income
def destroy(id: int, db: Session):
    income = db.query(models.Income).filter(models.Income.id == id)
    if not income.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The income with id {id} is not found") 
    income.delete(synchronize_session=False)
    db.commit()
    return "deleted!"



