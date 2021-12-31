def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
        # 6* func
        # 6*5 * func
        # 6*5 *4 func
       # 6*5 *4*3 func
       # 6*5 *4*3*2 func
       # 6*5*4*3*2*1 func


sum=recur_factorial(6)
print(f"{sum}............................")