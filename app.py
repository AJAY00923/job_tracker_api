from schemas import JobApplicationCreate, JobApplicationUpdate, Token, JobApplicationResponse

from typing import List
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from logger import logger
from database import engine, SessionLocal, Base
from models import JobApplicationDB
from sqlalchemy.orm import Session
from auth import create_access_token, verify_password, verify_token

Base.metadata.create_all(bind=engine)

app = FastAPI()

FAKE_USER = {
    "username": "ajay",
    "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW"
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload

@app.get("/")
async def read_root():
    return {"message": "Job Tracker Api is running!"}

@app.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> dict:
    if form_data.username != FAKE_USER["username"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not verify_password(form_data.password, FAKE_USER["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/applications")
async def get_applications(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
) -> dict:
    all_applications = db.query(JobApplicationDB).all()
    logger.info("Fetching all applications", total=len(all_applications))
    return {"applications": [JobApplicationResponse.model_validate(app) for app in all_applications]}

@app.post("/applications", status_code=201)
async def create_application(
    application: JobApplicationCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
) -> dict:
    db_application = JobApplicationDB(
        company=application.company,
        role=application.role,
        status=application.status
    )
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    logger.info("New application added", company=application.company, role=application.role)
    return {"message": "Application added successfully", "application": JobApplicationResponse.model_validate(db_application)}

@app.put("/applications/{company}")
async def update_application(
    company: str,
    update: JobApplicationUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
) -> dict:
    db_app = db.query(JobApplicationDB).filter(JobApplicationDB.company == company).first()
    if not db_app:
        raise HTTPException(status_code=404, detail=f"No application found for {company}")
    db_app.status = update.status
    db.commit()
    logger.info("Application updated", company=company, new_status=update.status)
    return {"message": f"Application for {company} updated to '{update.status}'"}

@app.delete("/applications/{company}")
async def delete_application(
    company: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
) -> dict:
    db_app = db.query(JobApplicationDB).filter(JobApplicationDB.company == company).first()
    if not db_app:
        raise HTTPException(status_code=404, detail=f"No application found for {company}")
    db.delete(db_app)
    db.commit()
    logger.warning("Application deleted", company=company)
    return {"message": f"Application for {company} deleted successfully"}