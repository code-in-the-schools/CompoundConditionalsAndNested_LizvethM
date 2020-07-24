#for loops
#outer loop
for i in range(10):
  print("Outer loop | i = " + str(i))
#inner loop
  for j in range(10):
    print("inner loop | i = "+ str(i)+ " | j = "+ str(j))
#nums are even
    if(i%2)==0 and (j%2)==0:
      print("even")


