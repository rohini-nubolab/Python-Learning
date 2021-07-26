def simple_interest(p, t, r):
  
    print("Principle amount is", p)
    print("Time period is", t)
    print("Interest is", r)

    si = (p * t* r)/100
    print("Simple interest is", si)
    
p = 1000
t = 2
r = 3
simple_interest(p, t, r)
