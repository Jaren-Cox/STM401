inp=input('Enter your Score: ')
try:
    gpa=float(inp)
except:
    inval=-1
try:
    if gpa >=0.9:
       print('Grade: A')
    elif gpa >=0.8:
      print('Grade: B')
    elif gpa >=0.7:
      print('Grade: C')
    elif gpa >=0.6:
        print('Grade: D')
    elif gpa <0.6:
     print('Grade: F')
except:
    print('Invalid input')