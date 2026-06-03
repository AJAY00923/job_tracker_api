from schemas import JobApplicationCreate, JobApplicationUpdate
from typing import List
from fastapi import FastAPI

app = FastAPI()

applications = []
@app.get("/")
def read_root():
    return {"message":"Job Tracker Api is running!"}

@app.get("/applications", response_model = dict)
def get_applications() -> dict:
    return {"applications": applications}

@app.post("/applications", status_code=201)
def create_application(application: JobApplicationCreate) -> dict:
    applications.append(application)
    return {"message": "Application added successfully", "application": application}

@app.put("/applications/{company}")
def update_application(company: str, update: JobApplicationUpdate) -> dict:
    for application in applications:
        if application.company == company:
            application.status = update.status
            return {"message": f"Application for {company} updated to '{update.status}'."}  

    return {'message' : f"NO Application found for  '{company}'."}

@app.delete("/applications/{company}")
def delete_application(company: str) -> dict:
    global applications
    for application in applications:
        if application.company == company:
            applications.remove(application)
            return {"message": f"Application for {company} deleted successfully."}
    return {"message": f"No application found for {company}."}  