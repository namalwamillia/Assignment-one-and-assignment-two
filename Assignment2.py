# # Finding the sum of items in a list
# sum=0
# list1=[1,2,3]
# for x in list1:
#   sum+=x

# print(sum)

# numbers=[3,5,9,7]
# # adding a number
# numbers.append(55)
# print(numbers)

# # size of a list
# print(len(numbers))

# # replacing a number
# numbers[0]=89
# print(numbers)


# a function finding the common values between 2 lists
def commonvalues(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(commonvalues([1,2,3,4,5], [5,6,7,8,9]))

