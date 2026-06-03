# def generator_function():
#     for i in range(5):
#         yield f"Application {i}"

# print("calling function...")
# result = generator_function()
# print("starting loop...")
# for app in result:
#     print(app)

def get_application_by_status(applications, status):
    for app in applications:
        if app.status == status:
            yield app

apps = [
    JobApplication("Google", "Backend Engineer"),
    JobApplication("Meta", "Data Engineer"),
    JobApplication("Apple", "Backend Engineer"),
]

apps[1].update_status("interview scheduled")

for app in get_application_by_status(apps, "applied"):
    print(app)