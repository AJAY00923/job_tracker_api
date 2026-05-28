class JobApplication:
    def __init__(self, company, role, status="applied"):
        self.company = company
        self.role = role
        self.status = status
       
    def describe(self):
        print(f"{self.role} at {self.company} is currently '{self.status}'.")

    @classmethod
    def from_string(cls, application_str):
        company, role = application_str.strip(",").split(",")
        return cls(company.strip(), role.strip())
    
    @classmethod
    def from_dict(cls, application_dict):
        return cls(application_dict["company"], application_dict["role"], application_dict.get("status", "applied"))
    
    @staticmethod
    def is_valid_status(status):
        valid_statuses = ["applied", "interview", "offer", "rejected"]
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

tech_app = TechApplication("Facebook", "Frontend Engineer", ["Python", "FastApi"])
remote_app = RemoteApplication("Amazon", "Data Scientist", "PST")
app = JobApplication("Google", "Backend Engineer")
tracked_app = TrackedApplication("Microsoft", "Software Engineer", 7)
print(tech_app)
print(repr(tech_app))
print(remote_app.is_compatible_with_time_zone("CST"))
print(remote_app.is_compatible_with_time_zone("PST"))
print(remote_app)
tech_app.update_status("interview scheduled")
print(tech_app)
print(tracked_app)
tracked_app.follow_up()
# Call it on the class directly — no object needed
print(JobApplication.is_valid_status("applied"))    # True
print(JobApplication.is_valid_status("interview"))  # True
print(JobApplication.is_valid_status("ghosted"))    # False

# You can also call it on an object — works both ways
app = JobApplication("Google", "Backend Engineer")
print(app.is_valid_status("offer"))  
if __name__ == "__main__":
    # --- TecahApplication ---
    tech_app = TechApplication("Facebook", "Frontend Engineer", ["Python", "FastApi"])
    remote_app = RemoteApplication("Amazon", "Data Scientist", "PST")
    app = JobApplication("Google", "Backend Engineer")
    tracked_app = TrackedApplication("Microsoft", "Software Engineer", 7)
    #--- Test __repr__ and __str__ ---
    print("==== Application DEtails ====")
    print(tech_app)
    print(repr(tech_app))
    
    # test time zone compatibility
    print("==== Time Zone Compatibility ====")
    print(remote_app.is_compatible_with_time_zone("CST"))
    print(remote_app.is_compatible_with_time_zone("PST"))

    # --- Test update status ---
    print("==== Update Status ====")
    tech_app.update_status("interview scheduled")
    print(f"after valid update: {tech_app}")
    tech_app.update_status("ghosted")
    print(f"after invalid update: {tech_app}")
    # --- Test Follow Up Remainder ---
    print("==== Follow Up Remainder ====")
    print(tracked_app)
    tracked_app.follow_up()
    # --- Test is_valid_status ---
    print("\n==== Valid Status Check ====")
    statuses = ["applied", "interview scheduled", "ghosted", "offer received"]
    for status in statuses:
        print(f"Is '{status}' a valid status? {JobApplication.is_valid_status(status)}")

    # --- Test class methods ---
    print("\n==== Class Methods ====")
    app_from_str = JobApplication.from_string("Netflix, Data Engineer")
    app_from_dict = JobApplication.from_dict({"company": "Apple", "role": "iOS Developer", "status": "offer"})
    print(app_from_str)
    print(app_from_dict)