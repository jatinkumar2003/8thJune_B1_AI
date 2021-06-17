# Question 2
print(5**9)
# o/p : 1953125

print(3//2)
# o/p : 1

print(7//3)
# o/p : 2

print(7/3)
# o/p : 2.3333333333335

print(6==6)
# o/p : True

a=20;a+=30;a%=3;print(a)
# 0/p : 2

print(True * False)
# o/p : 0

print(True & False)
# o/p : False

print(True and False)
# o/p : False

print(((6>3) and (7<4) or (18==3)) and (9>3))
# o/p : False

print(True is False)
# o/p : False

print('False' in 'False')
# o/p : True

print(((True == False) or (False > True)) and (False <= True))
# o/p : False

#******************************************

# Question 3
s1="Nice to have it"
s2=" here"
print(s1+s2)
# o/p : Nice to have it here

#******************************************

# Question 4
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])
# o/p : hello

#******************************************

# Question 5
a.insert(0,[s1]);a+=[s2]
print(a)
# o/p : [['Nice to have it'], 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, ' here']

#*****************************************

# Question 6
colour_list_1 = set(["white","black","red"])
colour_list_2 = set(["red","green"])
print(colour_list_1 - colour_list_2)
# o/p : {'white', 'black'}

#****************************************

# Question 7
a=set('abcdefghijklmnopqrstuvwxyz')
s=set('abcdefghijklmnopqrstuvwxyz')
if s==a:
   print('string is panagram')
else:
   print('not a panagram')
# o/p : string is panagram

#****************************************

# Question 8
print(eval('{0}+{0}{0}+{0}{0}{0}'.format(5)))
# o/p : 165

#***************************************

# Question 9
e=input("Enter comma seperated sequence of words :")
e=sorted(e.split(","))
print(",".join(e))
# o/p : Enter comma seperated sequence of words :without,hello,bag,world
#bag,hello,without,world

#**************************************

# Question 10
d={'student':['Rahul','Kishore','Vidya','Raakhi'],'marks':[57,87,67,79]}
d['marks']
m=max(d['marks'])
a=d['marks'].index(m)
print(d['student'][a])
# o/p : Kisore

#***************************************&*********************************
      

