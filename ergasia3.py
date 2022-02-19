#CHESS exercise

from random import seed
from random import randint



w_points=0
b_points=0

for rounds in range(0,100):

#place black queen
  b_q_x = randint(0, 7)
  b_q_y = randint(0, 7)


#place white castle but ensure it takes a different place from black queen
  w_c_x = b_q_x
  w_c_y = b_q_y
  while(w_c_x == b_q_x  and w_c_y == b_q_y):
    w_c_x = randint(0, 7)
    w_c_y = randint(0, 7)
 
#place white fool but ensure it takes a different place from black queen and white castle 
  w_f_x = b_q_x
  w_f_y = b_q_y
  while((w_f_x == b_q_x  and w_f_y == b_q_y) or (w_f_x == w_c_x  and w_f_y == w_c_y)):
    w_f_x = randint(0, 7)
    w_f_y = randint(0, 7)
    
    
    
    
#Check for points


#black points for queen  positions diagonally right up

  x=b_q_x
  y=b_q_y
  while(True):
    if(y ==0 or x==7):  #reached upper or right edge
      break
    y-=1
    x+=1
    if(x==w_c_x and y ==w_c_y): #castle is threatened
      b_points+=1
      break
    if(x==w_f_x and y ==w_f_y): #fool is threatened
      b_points+=1
#at the same time award white points
      w_points +=1
      break
  
#black points for queen  positions diagonally left down 

  x=b_q_x
  y=b_q_y
  while(True):
    if(y ==7 or x==0):  #reached lower or left edge
      break
    y+=1
    x-=1
    if(x==w_c_x and y ==w_c_y): #castle is threatened
      b_points+=1
      break
    if(x==w_f_x and y ==w_f_y): #fool is threatened
      b_points+=1
#at the same time award white points
      w_points +=1
      break
      
      
#black points for queen  positions diagonally right down

  x=b_q_x
  y=b_q_y
  while(True):
    if(y ==7 or x==7):  #reached lower or right edge
      break
    y+=1
    x+=1
    if(x==w_c_x and y ==w_c_y): #castle is threatened
      b_points+=1
      break
    if(x==w_f_x and y ==w_f_y): #fool is threatened
      b_points+=1
#at the same time award white points
      w_points +=1
      break
  
#black points for queen  positions diagonally left up 

  x=b_q_x
  y=b_q_y
  while(True):
    if(y ==0 or x==0):  #reached upper or left edge
      break
    y-=1
    x-=1
    if(x==w_c_x and y ==w_c_y): #castle is threatened
      b_points+=1   
      break
    if(x==w_f_x and y ==w_f_y): #fool is threatened
      b_points+=1
#at the same time award white points
      w_points +=1
      break

    
# points for queen same x with castle and fool
  if   w_c_x == b_q_x and w_f_x == b_q_x: 
#1st case queen is between
    if (b_q_y < w_c_y and b_q_y > w_f_y) or (b_q_y > w_c_y and b_q_y < w_f_y):
      b_points+=2
      w_points+=1
#2nd case castle is between
    if (w_c_y < b_q_y and w_c_y > w_f_y) or (w_c_y > b_q_y and w_c_y < w_f_y):
      b_points+=1
      w_points+=1  
#3d case fool is between
    if (w_f_y < b_q_y and w_f_y > w_c_y) or (w_f_y > b_q_y and w_f_y < w_c_y):
      b_points+=1

#points for queen same x with castle 
  elif w_c_x == b_q_x:
    b_points+=1
    w_points+=1
#points for queen same x with fool 
  elif w_f_x == b_q_x:
    b_points+=1
    
# points for queen same y with castle and fool
  if   w_c_y == b_q_y and w_f_y == b_q_y: 
#1st case queen is between
    if (b_q_x < w_c_x and b_q_x > w_f_x) or (b_q_x > w_c_x and b_q_x < w_f_x):
      b_points+=2
      w_points+=1
#2nd case castle is between
    if (w_c_x < b_q_x and w_c_x > w_f_x) or (w_c_x > b_q_x and w_c_x < w_f_x):
      b_points+=1
      w_points+=1  
#3d case fool is between
    if (w_f_x < b_q_x and w_f_x > w_c_x) or (w_f_x > b_q_x and w_f_x < w_c_x):
      b_points+=1

#points for queen same y with castle 
  elif w_c_y == b_q_y:
    b_points+=1
    w_points+=1
#points for queen same y with fool 
  elif w_f_y == b_q_y:
    b_points+=1


    
  print ("Queen is at ", b_q_x," ",b_q_y)
  print ("Castle is at ", w_c_x," ",w_c_y)
  print ("Fool is at ", w_f_x," ",w_f_y)
  print("White points ", w_points)
  print("Black points ", b_points)

#show chess board to check correct points
  for y in range (0,8):
    for x in range (0,8):
      if(y==b_q_y and x == b_q_x):
        print("Q",end=" ")
      elif(y==w_c_y and x == w_c_x):
        print("C",end=" ")
      elif(y==w_f_y and x == w_f_x):
        print("F",end=" ")
      else: 
        print("_",end=" ")
    print()

print ("Black points:", b_points)
print("White points:", w_points)