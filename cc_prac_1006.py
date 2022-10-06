#and a few more basic ones

#3Speciality
t=int(input())

for i in range (t):
    x,y,z=map(int,input().split())
    if x>y:
        if x>z:
            print('SETTER')
        else:
            print('EDITORIALIST')
    elif y>z:
        print('TESTER')
    else:
        print('EDITORIALIST')
        
 #4Ranklist
 
 
 t=int(input())

for i in range (t):
    x=int(input())
    if x%25==0:
        print(x//25)
    else:
        print(x//25+1)
        
  #5 Chef and happy string
  
t=int(input())

for i in range (t):
    s=input()
    n=len(s)
    i=0
    fg=0
    vow=['a','e','i','o','u']
    while i<=n-3:
        if s[i] in vow and s[i+1] in vow  and s[i+2]  in vow:
            print('Happy')
            fg=1
            break
        i+=1
    if fg==0:
        print('Sad')
        
  #Age Limit
  
  # cook your dish here
# cook your dish here
t=int(input())

for i in range (t):
    minn,maxx,s=map(int,input().split())
    if  s>=minn and s<maxx:
        print('yes')
    else:
        print('no')
        
        
    
            
            
        
