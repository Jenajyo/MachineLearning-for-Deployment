#1. Create 1st Tuple with values ->(10,20,30) and 2nd Tuple with values ->(40,50,60)
t1=(10,20,30)
t2=(40,50,60)


# a.Concatenate two tuples and store the values in "t_combine"
t_combine=t1+t2
t_combine


# b.Repeat the elements of "t_combine" 3 times
t_combine *= 3
t_combine


# c.Access 3rd element from "t_combine"
t_combine[2]


# d.Access first three elemens from "t_combine"
t_combine[:3]

# e.Access last three elemens from "t_combine"
t_combine[-3:]


# 2. Create a list 'my_list' with these elements:
# a.First element is a tuple values 1,2,3
# b.Second element is a tuple with values 'a','b','c'
# c.Thrid element is a tuple with values 'True','False'

my_list = [(1,2,3),("a","b","c"),(True,False)]
my_list


# 3. Append a new tuple (1,'a',True) to my_list
my_list.append((1,'a',True))
my_list

#a.Append a new list ["sparta",123] to my_list
my_list += ["sparta",123]
my_list

#4 Create a dictionary 'fruit' where:
# a.The first key is 'fruit' and the values are ("Apple","Banana","Guava","Mango")
# b.The second key is cost and the values are (85,54,120,70)
fruit={'fruit':["Apple","Banana","Guava","Mango"],'cost':[85,54,120,70]}
fruit

# c. Extract all the keys from fruit
fruit.keys()


# d. Extract all the values from fruit
fruit.values()

# 5. Create a set named 'my_set' with values (1,1,"a","a",True,True)
my_set={1,1,"a","a",True,True}
my_set

