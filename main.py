class JobApplication:
    def __init__(self, company, role, status="applied"):
        self.company = company
        self.role = role
        self.status = status
       
       

    def update_status(self, new_status):
        self.status = new_status
    

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