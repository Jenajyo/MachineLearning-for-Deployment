#1 . Create 2 lists l1 and l2,where l1 has values -> [1,2,3,4,5,6] and l2 has values [6,5,4,3,2,1]
#  a.Compare the correspoding element values of both lists and print "l1 element value is greater than l2 element value
#   if correspoding l1 value is greater else print "l1 element value is less than l2 element value " if corresponding element value
#.   value is less than l2

l1=[1,2,3,4,5,6]
l2=[6,5,4,3,2,1]
for i in range(0,len(l1)):
    if l1[i]>l2[i]:
        print('L1 element value is greater than L2 element value')
    elif l1[i]<l2[i]:
        print('L1 element value is less than L2 element value')


#2. Create a Tupule with Values (10,20,30,40,50) Use a loop to add 5 more to each element of the tupule
tup=(10,20,30,40,50)
tup=tuple(x+5 for x in tup)
tup

# 3.Create a user defined function "add_10()" which will add 10 more to whatever value you pass in the function.

def add_10(a):
    if type(a)==str:
        return a+'10'
    elif type(a)==int:
        return a+10
    elif type(a)==list:
        return a.append(10)
    
# 4. Create a user defined function "check_odd_even()" which will check whether given integer value is odd or even .
# if the number is odd print "Odd Number" else print "even number"

def check_odd_even(num):
    if num%2==0:
        print('Even')
        
        