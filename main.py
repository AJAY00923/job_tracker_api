from datetime import date
class JobApplication:
    def __init__(self, company, role, status="applied", created_at=None):
        self._company = company
        self._role = role
        self._status = None
        self.status = status
        self._created_at = created_at if created_at is not None else date.today()

    # --- Properties ---
    @property
    def company(self):
        return self._company    
    @company.setter
    def company(self, new_company):
        if not new_company or not new_company.strip():
            raise ValueError("Company name cannot be empty.")
        self._company = new_company.strip()

    
    @property
    def role(self):
        return self._role
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):
        valid_statuses = ["applied", "interview scheduled", "offer received", "rejected"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid options are: {', '.join(valid_statuses)}")
        self._status = new_status
    
    @property
    def created_at(self):
        return self._created_at
#---- methods ---
    def __hash__(self):
        return hash((self.company, self.role))
    def __lt__(self, other):
        if not isinstance(other, JobApplication):
            return NotImplemented
        return self.company.lower().strip() < other.company.lower().strip()

    def __eq__ (self, other):

      return self.company == other.company and self.role == other.role
   
    def describe(self):
        print(f"{self._role} at {self._company} is currently '{self._status}' . ")
    @classmethod
    def from_string(cls, application_str):
        company, role = application_str.strip(",").split(",")
        return cls(company.strip(), role.strip())
    
    @classmethod
    def from_dict(cls, application_dict):
        return cls(application_dict["company"], application_dict["role"], application_dict.get("status", "applied"))
    
    @staticmethod
    def is_valid_status(status):
        valid_statuses = ["applied", "interview scheduled", "offer received", "rejected"]
        return status in valid_statuses

    def update_status(self, new_status):
        if self.is_valid_status(new_status):
            self.status = new_status
        else:
            print("Invalid status. Please choose a valid status.")

    def __repr__(self):
        return f"JobApplication(company={self.company!r}, role={self.role!r}, status={self.status!r})"
    
    def __str__(self):
        return f"Application for {self.role} at {self.company} is currently '{self.status}'."
    
class TechApplication(JobApplication):
    def __init__(self, company, role, tech_stack, status ="applied"):
        super().__init__(company, role, status)
        self.tech_stack = tech_stack

    def __repr__(self):
         return f"TechApplication(company={self.company!r}, role={self.role!r}, tech_stack={self.tech_stack!r}, status={self.status!r})"
    
class RemoteApplication(JobApplication):
    def __init__(self, company, role, time_zone, status="applied"):
        super().__init__(company, role, status)
        self.time_zone = time_zone
    
    def is_compatible_with_time_zone(self, other_time_zone):
        return self.time_zone == other_time_zone

    def __repr__(self):
        return f"RemoteApplication(company={self.company!r}, role={self.role!r}, time_zone={self.time_zone!r}, status={self.status!r})" 
# Test it like this:
    

class FollowUpRemainder:
    def __init__(self, days):
        self.days = days
    def remind(self, application):
        print(f"Reminder: Follow up on your application for {application.role} at {application.company} in {self.days} days.")

class TrackedApplication(JobApplication):
    def __init__(self, company, role,follow_up_days, status="applied"):
        super().__init__(company, role, status)
        self.follow_up_remainder = FollowUpRemainder(follow_up_days)

    def follow_up(self):
        self.follow_up_remainder.remind(self)



class ApplicationTracker:
    def __init__(self):
        self.applications = []
    
    def add(self, application):
        self.applications.append(application)
        # you write this
    
    def get_by_status(self, status):
        return [app for app in self.applications if app.status == status]
        # you write this
     
    def summary(self):
        # you write this
        print("==== Application Summary ====")
        if not self.applications:
           raise ValueError("No applications to summarize.")
        status_counts = {}
        for app in self.applications:
            status_counts[app.status] = status_counts.get(app.status, 0) + 1
        for status, count in status_counts.items():
            print(f"{status}: {count} applications")

#-- Application Generator ---           
def get_application_by_status(applications, status):
    for app in applications:
        if app.status == status:
            yield app
            
if __name__ == "__main__":
   tracker = ApplicationTracker()
   tracker.add(JobApplication("Netflix", "Backend Engineer"))
   tracker.add(JobApplication("Meta", "Data Engineer"))
   tracker.add(TechApplication("OpenAI", "AI Engineer", ["Python", "FastAPI"]))
   tracker.summary()
   app1 = JobApplication("Google", "Backend Engineer")
   app2 = JobApplication("Google", "Backend Engineer")
   app3 = JobApplication("Meta", "Backend Engineer")
   apps = [
    JobApplication("Meta", "Backend Engineer"),
    JobApplication("Apple", "Backend Engineer"),
    JobApplication("Google", "Backend Engineer"),
]
   apps[1].update_status("interview scheduled")

   sorted_apps = sorted(apps)
   for app in sorted_apps:
    print(app.company)
   print(app1 == app2)  # what prints?
   print(app1 == app3)  # what prints?  
   app1 = JobApplication("Google", "Backend Engineer")
   apps = {app1}
   print(apps)
   for app in get_application_by_status(apps, "applied"):
    print(app)