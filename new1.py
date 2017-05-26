'''
z=1
for z in range (1,11):
    print(z)
'''
      
    #for loop  basic structure  
    #will print depending how u do it ex 1 ex 2 ***IN*** keyword
'''
x = [1,2,3,1,23,4,2,]
x = range(1,10)

print (x ,'range_in_string')
'''   
#infinte loop 
'''
while z < 20:
    #print ('something2')
'''
    
'''  
z = 1
if(z == 1):
    print ('something2')
 
'''   
    
# u can use if  and do whatever  u want   
'''
ex    
if  2 < 4 >67 <= 68 :  can go as long as one wants 
print () 
'''

'''
if condition :
   print ()
elif condition :
      print ()
else condition :
      print ()
else: print()      
u can use  or  like 'or' instead of || and 'and' instead of &&
'''
 # basic function 
'''
def fun_Name():
   x = 1 
   y = 3 
   print (x + y + y)


fun_Name()
'''
# basic pramenters
'''
def fun_Name(num1,num2,num3):
  answer = num1 + num2 * num3
  return answer 

x = fun_Name(6,44,89) 
print(x)
'''

'''
def fun_Name1(string1,string2,string3):
  answer = string1 + string2 + string3
  return answer 
z = fun_Name1('hello','what','why')
  
print(z)
'''
# another ex define n other pramenters
'''
def fun_Name1(background ,color,font_size ,etc):
  print('bg',background)
  print('co',color)
  print('fs',font_size)
  print('etc',etc)
  
fun_Name1('black','red','12','etc')
'''

# another ex
'''
def fun_Name1(background ,color,font_size ,etc):
  print('bg',background)
  print('co',color)
  print('fs',font_size)
  print('etc',etc)
    
fun_Name1(
  background ='black',
  color ='red',
  font_size = '12',
  etc ='etc') 
  
'''
# u can also define defaults ///// the way to go
''
def fun_Name1(background ='black',
              color ='red',
              font_size = '12',
              etc ='etc'):
  
  
  print('bg',background)
  print('co',color)
  print('fs',font_size)
  print('etc',etc)
  
#### u can also change a default by specifiying a paramenter

fun_Name1(background = 'grey')

'''

# defining  a global var vs local   sometimes not def global is the route to go


#writing to a file 

# the w in the paramenter stands for write 
'''
writeMe = 'example text'
saveFile = open('exampleWrite.txt','w')
saveFile.write(writeMe)
saveFile.close()


appendMe = 'other text'
saveFile = open('exampleFile.txt','a')
saveFile .write('\n')
saveFile.write(appendMe)
saveFile.close()
'''

#reading from a file
'''
readMe = open('exampleFile.txt','r').read()
print(readMe)

#u can also split and it will come back in a list 

splitMe = readMe.split('\n')
print(splitMe)

#also u can use the readlines function and it will also put in a list 

readMe2 = open('exampleFile.txt','r').readlines()
print(readMe2)


#x =2147483647

#if(aa == bb):
   # print ("syntax  correct")
   
 #for loop  basic structure  
 
#x = [1,2,3,1,23,4,2,]
#for something in x:
   # print (something)
    
 # counter for loop in range
 
#for z in range(1,43):
  #  print (z)

'''
#classes when defining just say class inbed your functions 
#to call the class use calc.  add mult etc 
'''
class calc:
    
    def add(x,y):
        answer = x + y
        print(answer)
        
    def sub(x,y):
        answer = x - y
        print(answer)    
        
    def mult(x,y):
        answer = x * y
        print(answer)
        
    def div(x,y):
        answer = x / y
        print(answer)
        
