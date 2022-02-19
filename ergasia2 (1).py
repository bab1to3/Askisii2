#FILE exercise

fo = open("original.txt",'r') 
data = fo.read()
new_data=""
print(len(data))

for x in range(0,len(data)):
  if data[x] == '\n':
    new_data+=' '
  if (data[x]>= 'a' and data[x] <='z') or (data[x] ==' ') or (data[x]>= 'A' and data[x] <='Z'):
    new_data+=data[x]
#print(new_data)
list1= new_data.split(" ")
#take away spaces as words
total_words=len(list1)
x=0
while(True):
  if x==len(list1):
    break
  if list1[x]=='':
    list1.pop(x)
    continue
  else:
    x+=1
    continue
print (list1)
total_words=len(list1)
x=0
while(True):
  if x==len(list1) :
    break
  found=False
  for y in range(1,total_words):

    if(len(list1[x]) + len(list1[y]) ==20):
      
      total_words -=2
#      print(total_words," ",x," ",list1[x]," ",y," ", list1[y] )
#      input()
      list1.pop(x)
      list1.pop(y)
      found=True
      break
  if found == False:
    x+=1
    continue
#find max word length 
max = len(list1[0])
for x in range (0, len(list1)):
  if max < len(list1[x]):
    max=len(list1[x])
#check for lengths up tp max
total_words= len(list1)
test_length=1

for x in range (1, max):
  test_words=0
  for y in range (0, len(list1)):
    if(len(list1[y])==x):
      test_words+=1
  print("Length: ", x, " Words: ", test_words)
    
  



  

fo.close();
 
    