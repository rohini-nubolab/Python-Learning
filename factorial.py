# Python 3 program to find 
# factorial of given number 
  
def factorial(N): 
  
    # single line to find factorial 
    return 1 if (N==1 or N==0) else N * factorial(N - 1)  
  
  
# Driver Code 
N = 3
print ("Factorial of",N,"is", factorial(N)) 
