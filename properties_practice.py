from datetime import date 
class JobApplication:
    def __init__(self, company, role, status="applied"):
        self._company = company
        self._role = role
        self._status = status
        self._created_at = date.today()
    
    @property
    def created_at(self):
        return self._created_at
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        valid_statuses = ["applied", "interview scheduled", "offer received", "rejected"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid options are: {', '.join(valid_statuses)}")
        self._status = new_status
    
    def __str__(self):
        return f"Application for {self._role} at {self._company} is currently '{self._status}'."
    @property
    def company(self):
        return self._company        
    
    @company.setter
    def company(self, new_company):
        if not new_company or not new_company.strip():
            raise ValueError("Company name cannot be empty.")
        self._company = new_company.strip()
# Test it like this:
app = JobApplication("Google", "Backend Engineer")
print(app)  # Application for Backend Engineer at Google is currently 'applied'.
app.status = "interview scheduled"
print(app)  # Application for Backend Engineer at Google is currently 'interview scheduled'.
app.company = "Meta"
print(app.company)  # Application for Backend Engineer at Meta is currently 'interview scheduled'.
#app.company = ""
print(app.company)  # This will raise a ValueError: Company name cannot be empty.
try:
    app.status = "ghosted"  # This will raise a ValueError
except ValueError as e:
    print(e)  # Invalid status. Valid options are: applied, interview scheduled, offer received, rejected   
print(app.created_at)  
# app.created_at = "2020"# 2024-06-01 (or today's date)