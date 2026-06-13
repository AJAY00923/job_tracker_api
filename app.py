from email.mime import application

from schemas import JobApplicationCreate, JobApplicationUpdate
from typing import List
from fastapi import FastAPI, HTTPException
from logger import logger   
from database import engine, SessionLocal, Base
from models import JobApplicationDB
from sqlalchemy.orm import Session
from fastapi import Depends

Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

applications = []
@app.get("/")
async def read_root():
    return {"message":"Job Tracker Api is running!"}

@app.get("/applications", response_model = dict)
async def get_applications(db: Session = Depends(get_db)) -> dict:
    all_applications = db.query(JobApplicationDB).all()
    logger.info("Fetching all applications", total=len(all_applications))
    return {"applications": all_applications}

@app.post("/applications", status_code=201)
async def create_application(application: JobApplicationCreate, db: Session = Depends(get_db)) -> dict:
    applications.append(application)
    logger.info("New application added", company=application.company, role=application.role)
    return {"message": "Application added successfully", "application": application}

@app.put("/applications/{company}")
async def update_application(company: str, update: JobApplicationUpdate) -> dict:
    db_application = JobapplicationDB(
        company=application.company, 
        role=application.role, 
        status=application.status
        )
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    logger.info("New Application Added", company=application.company, role=application.role)
    return {"message": f"Application for {company} Added successfully."}

@app.delete("/applications/{company}")
async def delete_application(company: str) -> dict:
    global applications
    for application in applications:
        if application.company == company:
            applications.remove(application)
            logger.warning("Application deleted", company=company)
            return {"message": f"Application for {company} deleted successfully."}
    raise HTTPException(status_code=404, detail=f"Application for {company} not found.")  