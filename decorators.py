import time
def validate_input(func):
    def wrapper():
        print("validating...")
        func()
        print("validation complete.")
        
    return wrapper
                

@validate_input
def say_hello():
    print("Hello, world!")

say_hello()

def timer(func):
    def wrapper(n):
        s_time = time.time()
        result = func(n)
        e_time = time.time()
        print(f"Execution_time: {e_time - s_time:.4f} seconds ")
        return result
    return wrapper

@timer
def compute_squares(n):
    return [i**2 for i in range(n)]     

compute_squares(1000000)
        
squares = compute_squares(1000000)
print(squares)