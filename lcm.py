 def get_lcm(n1, n2):
     if n1 > n2:
         tar = n1
     else:
         tar = n2
     i = 1

     while True:
         if tar%n1==0 and tar%n2==0:
             print(f"{tar} is the LCM of {n1} and {n2}")
             break
         else:
             i += 1
             tar *= i

get_lcm(2, 13)
