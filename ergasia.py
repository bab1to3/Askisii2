

#function places picks random kapaki from remaining kapakia and places it  at random place in matrix which is empty or contains lower kapaki. Continues until it succeeds
def place_kapaki(total_remaining):
#  print(total_remaining)
  places=[]
  while True:

    if  len(places)==0:
      places=[0,1,2,3,4,5,6,7,8] j
      value = randint(0, total_remaining-1)
      new_kapaki = kapakia[value] 
#    print("WHILE TRUE ", len(places))
#    print(places)
    y=randint(0,len(places)-1)
    new_place=places[y]
    v_place  = new_place//3
    h_place  = new_place-v_place*3

    content = matrix[v_place][h_place]
    if content =="N" or content< new_kapaki:
      matrix[v_place][h_place] = new_kapaki
      return value
     
    else:
      places.pop(y)
      continue
      
  

#function checks status of matrix and returns true when game needs to end or false when game needs to continue
def check_end(m):
  #Horizontal
  r1=m[0][0]+m[0][1]+m[0][2]
  r2=m[1][0]+m[1][1]+m[1][2]
  r3=m[2][0]+m[2][1]+m[2][2]
  if r1=="ABC" or r1=="CBA" or r2=="ABC" or r2=="CBA" or r3=="ABC" or r3=="CBA"  :
    return True
  
  #check for equals
  if r1=="AAA" or r1=="BBB" or r1=="CCC" or  r2=="AAA" or r2=="BBB" or r2=="CCC" or  r3=="AAA" or r3=="BBB" or r3=="CCC" :
    return True 
    
    
  #Vertical
  r1=m[0][0]+m[1][0]+m[2][0]
  r2=m[0][1]+m[1][1]+m[2][1]
  r3=m[0][2]+m[1][2]+m[2][2]
  if r1=="ABC" or r1=="CBA" or r2=="ABC" or r2=="CBA" or r3=="ABC" or r3=="CBA"  :
    return True
  
  #check for equals
  if r1=="AAA" or r1=="BBB" or r1=="CCC" or  r2=="AAA" or r2=="BBB" or r2=="CCC" or  r3=="AAA" or r3=="BBB" or r3=="CCC" :
    return True
        
   #Diagonal
  r1=m[0][0]+m[1][1]+m[2][2]
  r2=m[0][2]+m[1][1]+m[2][0]
  if r1=="ABC" or r1=="CBA" or r2=="ABC" or r2=="CBA":
  	return True
   #check for equals  
  if r1=="AAA" or r1=="BBB" or r1=="CCC" or r2=="AAA" or r2=="BBB" or r2=="CCC":
  	return True
  return False
   
total_tries=0;  
total_rounds=100
for rounds in range(total_rounds):  
  matrix = [["N", "N", "N"],["N", "N", "N"],["N", "N", "N"]]
  kapakia =["A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C"]
  remaining=27
  for x in range(27):
   
#    print("X is ",x)
#    print(matrix)
#    print(kapakia)
    remove=place_kapaki(remaining)   
#    print(remove)
    remaining-=1
    kapakia.pop(remove)
#    print ("New Matrix")
#    for r in matrix:
#     for c in r:
#        print(c,end=" ")
#     print()
    if check_end(matrix):
      break
  total_tries+=x-1
#  print(rounds)

print (total_tries/total_rounds);




    

