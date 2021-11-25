from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authendication, income, suppliers, staff, outcome, notes, shift, fixedCost
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi_pagination import add_pagination

# Deta
# Project Key: a07rzxne_PYUWRDdTuQBKZka9h5Y9UNDFcZC3Qvah
# Project ID: a07rzxne

# On video 3:30
# TODO
# repository/delete problem

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authendication.router)
app.include_router(user.router)
app.include_router(notes.router)
app.include_router(blog.router)
app.include_router(income.router)
app.include_router(suppliers.router)
app.include_router(staff.router)
app.include_router(outcome.router)
app.include_router(shift.router)
app.include_router(fixedCost.router)


# app.router.redirect_slashes = False

origins = ["*"]
# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:8000",
#     "http://localhost:5500/frontend/",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_pagination(app)
