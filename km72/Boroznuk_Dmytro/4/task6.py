import time
print("Can the chess tour carry out the move?")
x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
if x1==x2 or y1==y2:
  print("Yes")
else:
  print("No")
time.sleep(3)
