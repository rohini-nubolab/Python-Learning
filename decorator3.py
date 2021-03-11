def hello_decorator(func): 
    def inner1(*args, **kwargs): 
          
        returned_value = func(*args, **kwargs) 
        return returned_value 
          
    return inner1 

@hello_decorator
def sum_two_numbers(a, b): 
    return a + b 
  
a, b = 1, 2
  
print("Sum =", sum_two_numbers(a, b)) 
