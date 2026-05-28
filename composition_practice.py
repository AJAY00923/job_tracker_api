#component class - stands alone and  knows nothing about JOb
class Salary:
    def __init__(self, amount, currency='USD'):
        self.amount = amount
        self.currency = currency
    def display(self):
        return f"{self.amount} {self.currency}"
    
#componenet class - standalone
class Location:
    def __init__(self, city, country):
        self.city = city
        self.country = country

    def display(self):
        return f"{self.city}, {self.country}"
    
# Main class - HAS a Salary and Location
class JobOffer:
    def __init__(self, company, role, salary_amount, city, country):
        self.company = company
        self.role = role
        self.salary = Salary(salary_amount)  # Composition: JobOffer HAS a Salary
        self.location = Location(city, country)  # Composition: JobOffer HAS a Location

    def summary(self):
        print(f"Role: {self.role} at {self.company}")
        print(f"Salary: {self.salary.display()}")
        print(f"Location: {self.location.display()}")

offer = JobOffer("Google", "Software Engineer", 120000, "Mountain View", "USA")
offer.summary()