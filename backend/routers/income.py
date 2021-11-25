from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import user, income
from fastapi_pagination import pagination_params, Page, paginate
# from fastapi_pagination.limit_offset import pagination_params

router = APIRouter(
    prefix="/api/income",
    tags=['Income']
)

get_db = database.get_db

# @router.get('/', response_model=List[schemas.ShowIncome])
@router.get('/', response_model=Page[schemas.ShowIncome], dependencies=[Depends(pagination_params)])
async def all_income(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return paginate(income.get_all(db))

@router.get('/{year}/{month}/', response_model=Page[schemas.ShowIncome], status_code=200, dependencies=[Depends(pagination_params)])
async def show_income_by_date(year: str, month: str , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return paginate(income.show_by_date(year, month, db))

@router.get('/{id}', status_code=200, response_model=schemas.ShowIncome)
async def show_income(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return income.show(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_income(request: schemas.Income, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return income.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
async def destroy_income(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return income.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_income(id:int , request: schemas.Income, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return income.update(id, request, db) 

