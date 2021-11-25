from typing import List, Optional
from datetime import date
# datetime, time
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class NotesIn(BaseModel):
    date: Optional[date]
    title: Optional[str] = None
    body: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    author_id: Optional[int]

class NotesOut(BaseModel):
    id: Optional[int]
    date: Optional[date]
    title: Optional[str]
    body: Optional[str]
    tags:  Optional[str] 
    active:  Optional[bool]
    author_id: Optional[int]
    class Config():
        orm_mode = True

class BlogBase(BaseModel):
    id: Optional[int] = None
    date: Optional[date] 
    title: Optional[str] = None
    body: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    # author_id: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    # Refers to the first class Blog
    the_blogs: List[Blog] = []
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    id: int
    date: Optional[date] 
    title: Optional[str] = None
    body: Optional[str] = None
    tags: Optional[str] = None
    active: Optional[bool] = False
    owner: ShowUser
    class Config():
        orm_mode = True

class login(BaseModel):
    username: str
    password: str

class Suppliers(BaseModel):
    id: int
    company_name: Optional[str] = None
    responsible: Optional[str] = None
    address: Optional[str] = None
    telephone: Optional[str] = None
    email: Optional[str] = None
    payment_way: Optional[str] = None
    notes: Optional[str] = None
    # email: Optional[EmailStr] = None
    # the_outcome: ShowOutcome
    class Config():
        orm_mode = True


class FixedCost(BaseModel):
    id: int
    name: Optional[str] = None
    class Config():
        orm_mode = True


class Shift(BaseModel):
    id: int
    service_name_1: Optional[str] = None
    barman_name_1: Optional[str] = None
    service_name_2: Optional[str] = None
    barman_name_2: Optional[str] = None
    notes: Optional[str] = None
    # the_outcome: List[Outcome] = []
    class Config():
        orm_mode = True

class StaffBase(BaseModel):
    id: int
    name: Optional[str] = None
    position: Optional[str] = None
    active: Optional[bool] = False
    daily_salary: Optional[float] = None
    insurance: Optional[float] = None
    notes: Optional[str] = None
    # the_outcome: List[Outcome] = []
    # income: Income

class Staff(StaffBase):
    class Config():
        orm_mode = True
    

class Outcome(BaseModel):
    id: int
    date: date
    description: Optional[str] = None
    invoice_number: Optional[str] = None
    cost: Optional[float] = None
    extra_cost:  Optional[float] = None
    tax_perc: Optional[int] = None
    tax_perc2:  Optional[int] = None
    supplier_id:  Optional[int] = None
    staff_id:  Optional[int] = None
    fixed_cost_id: Optional[int] = None
    is_variable_cost: Optional[bool] = False
    is_fix_cost:  Optional[bool] = False
    is_purchase_cost:  Optional[bool] = False
    is_salary_cost:  Optional[bool] = False
    is_insurance_cost:  Optional[bool] = False
    is_misc_cost:  Optional[bool] = False
    payment_way:  Optional[str] = None
    is_paid:  Optional[bool] = False
    outcome_notes: Optional[str] = None
    # image: Optional[HttpUrl] = None

    # the_staff: List[ChildSchema] = None
    class Config():
        orm_mode = True

class OutcomeDetails(BaseModel):
    id: int
    outcome_id: int
    product_name: Optional[str] = None
    product_description: Optional[str] = None
    price_per: Optional[float] = None
    amount: Optional[int] = None
    tax: Optional[int] = None
    notes: Optional[str] = None
    # the_outcome: List[Outcome] = []
    class Config():
        orm_mode = True


class ShiftBase(BaseModel):
    id: int
    service_id_1: Optional[int] = None
    barman_id_1: Optional[int] = None
    service_id_2: Optional[int] = None
    barman_id_2: Optional[int] = None

class Shift(ShiftBase):
    class Config():
        orm_mode = True

class IncomeBase(BaseModel):
    id: int
    date: date
    service_income_1: Optional[float] = None
    service_income_2: Optional[float] = None
    bar_income_1: Optional[float] = None
    bar_income_2: Optional[float] = None
    pos: float = 0
    z_count: float = 0
    vat: float = 0
    waitress_1: Optional[str] = None
    waitress_2: Optional[str] = None
    barman_1: Optional[str] = None
    barman_2: Optional[str] = None
    notes: Optional[str] = None
    shift_id: str
    

class Income(IncomeBase):
    class Config():
        orm_mode = True

class ShowIncome(IncomeBase):
    id: Optional[int]
    date: Optional[date]
    service_income_1: Optional[float] = None
    service_income_2: Optional[float] = None
    bar_income_1: Optional[float] = None
    bar_income_2: Optional[float] = None
    pos: float = 0
    z_count: float = 0
    vat: float = 0
    waitress_1: Optional[str] = None
    waitress_2: Optional[str] = None
    barman_1: Optional[str] = None
    barman_2: Optional[str] = None
    notes: Optional[str] 
    shift_id: Optional[str]
    the_shift: Optional[Shift] 

    class Config():
        orm_mode = True