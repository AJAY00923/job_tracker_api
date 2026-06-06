from schemas import JobApplicationCreate, JobApplicationUpdate
from typing import List
from fastapi import FastAPI
from logger import logger   

app = FastAPI()

applications = []
@app.get("/")
async def read_root():
    return {"message":"Job Tracker Api is running!"}

@app.get("/applications", response_model = dict)
async def get_applications() -> dict:
    logger.info("Fetching all applications", total=len(applications))
    return {"applications": applications}

@app.post("/applications", status_code=201)
async def create_application(application: JobApplicationCreate) -> dict:
    applications.append(application)
    logger.info("New application added", company=application.company, role=application.role)
    return {"message": "Application added successfully", "application": application}

@app.put("/applications/{company}")
async def update_application(company: str, update: JobApplicationUpdate) -> dict:
    for application in applications:
        if application.company == company:
            application.status = update.status
            logger.info("Application updated", company=company, new_status=update.status)
            return {"message": f"Application for {company} updated to '{update.status}'."}  

    return {'message' : f"NO Application found for  '{company}'."}

@app.delete("/applications/{company}")
async def delete_application(company: str) -> dict:
    global applications
    for application in applications:
        if application.company == company:
            applications.remove(application)
            logger.warning("Application deleted", company=company)
            return {"message": f"Application for {company} deleted successfully."}
    return {"message": f"No application found for {company}."}  