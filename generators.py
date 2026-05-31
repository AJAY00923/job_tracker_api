def generator_function():
    for i in range(5):
        yield f"Application {i}"

print("calling function...")
result = generator_function()
print("starting loop...")
for app in result:
    print(app)