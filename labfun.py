

##Intro Lab
# What version of Python am I using
import sys 
print(sys.version)

#print a number type
print(type(1.4))
print("")
print("")
print('Hello, World!!!')
print("")


my_variable = 1


#stringfun
cats_names = "Samone & Rayleigh"
print("")
print(cats_names)
print("")
print("the first letter is:")
print(cats_names[0])
print(cats_names[-len(cats_names)])


##Tuples lab
#Basics
tuple1 = ("disco", 10, 1.2)
print("")
print("tuple1 is",type(tuple1))
print("")
print("What are the arguments of tuple1?")
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print("")
print("Tuples are immutable!")
print("")
print("What are the arguments of tuple1 in reverse using reverse indexing?")
print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-3])
print("")
print("What are the types of the arguments of tuple1 in reverse using reverse indexing?")
print(type(tuple1[-1]))
print(type(tuple1[-2]))
print(type(tuple1[-3]))
print("")

#Concatenate and slice tuples
tuple1 = tuple1 + ("hardrock",10)
print("To slice tuples, you have to use an end index one greater than the index value of the tuple.")
print("The command tuple1[0:5] outputs the following five elements.")
print(tuple1[0:5])
print("")
print("... even though tuple1[4] = ",tuple1[4])
tuple2 = tuple1
len(tuple2)

#Sorting
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
RatingsSorted = sorted(Ratings)

C_tuple = (-5,1,-3)
C_tupleSorted = sorted(C_tuple)
C_tuple


#Nesting
print("")
print("Tuples can be nested.")
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])
print("Let's get to the bottom of the tree!")
print(NestedT[4][1][0])
print(NestedT[4][1][1])


##Lists lab
# Create and index a list
print("")
print("Create a List")
L = ["Cyndi Lauper", 10.1, 1982]
print(L)
print("")
print("Use positive and negative indexing to print the same elements.")
print("")
print("The first element is the following (using positive indexing). \n", L[0])
print("\n The first element (using negative indexing) is the following. \n",L[-len(L)])
print("\n The second element is the following (using positive indexing). \n", L[1])
print("\n The second element (using negative indexing) is the following. \n",L[-len(L)+1])
print("\n The third element is the following (using positive indexing). \n", L[len(L)-1])
print("\n The third element (using negative indexing) is the following. \n",L[-1])
print("")
print("Lists can contain tuples.")
L2 = ["Cyndi Lauper", 10.1, 1982, [1, 2], ("A", 1)]
print("\n",L2)
#List mutations
print("")
print("Lists are mutable.")
L = ["Cyndi Lauper", 10.1, 1982,"CL",1]
print("\n Now the list L from above contains the following elements.\n", L)
print("")
print("List slicing operations, like L[3:5], produce the following results. \n",L[3:5])
print("")
print("Extend and append have different functional results. \n Extend adds elements to a list as individual elements while append adds the elements as a list for instance.")
print("\n Redefine L as the following.")
L = ["Cyndi Lauper", 10.1]
print("\n",L)
L.extend(['pop',14])
print("\n Now extend L with ['pop', 14]. \n",L)
print("\n Redefine L as the following.")
L = ["Cyndi Lauper", 10.1]
print("\n",L)
L.append(['pop',14])
print("\n Now append L with ['pop', 14]. \n",L)
print("")
Lnew = ["BeeGees",10.3,1,"disco"]
print("Here are some mutations possible with a new list called Lnew. \n", Lnew)
Lnew[0] = "Lizzo"
Lnew[3] = "pop"
print("With the commands Lnew[0] = 'Lizzo' and Lnew[3] = 'pop', the variable Lnew becomes the following.", Lnew)
print("")
del(Lnew[3])
print("\n With the command del(Lnew[3]), Lnew becomes the following. \n",Lnew)
#List splits
print("")
print("The split function splits strings into a list.")
print("\n For instance, the 'hard rock'.split() uses the default character for splitting, the space. \n", 'hard rock'.split())
print("")
A = "A,B,C,D"
Asplit = A.split(",")
print("Here is an example of splitting on a comma for a new string variable A and assigned the result to a new variable Asplit. \n A = ",A,"\n Asplit = ",Asplit)
#Copying and cloning
print("")
B = Asplit
print("When you copy a variable, the variables both reference the same elements in memory. For instance, consider the opearation B = Asplit. \n B = ",B)
Asplit[1] = "banana"
print("\n When an element of A is changed, B is changed also. Here is the result of B after the operation Asplit[1] = 'banana.' \n B = ", B)
print("Let's now reassign")








