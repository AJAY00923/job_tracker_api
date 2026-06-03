from fastapi import FastAPI
from schemas import JobApplicationCreate

app = FastAPI()

applications = []
@app.get("/")
def read_root():
    return {"message":"Job Tracker Api is running!"}

@app.post("/applications")
def create_application(application: JobApplicationCreate):
    applications.append(application)
    return {"message": "Application added successfully", "application": application}

@app.get("/applications")
def get_applications():
    return {"applications": applications}