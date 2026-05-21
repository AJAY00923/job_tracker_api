class JobApplication:
    def __init__(self, company, role, status="applied"):
        self.company = company
        self.role = role
        self.status = status
        # your code
       

    def update_status(self, new_status):
        self.status = new_status
    

    def __repr__(self):
        return f"JobApplication(company='{self.company}', role='{self.role}', status='{self.status}')"

# Test it like this:
app = JobApplication("Google", "Backend Engineer")
print(app)
app.update_status("interview scheduled")
print(app)