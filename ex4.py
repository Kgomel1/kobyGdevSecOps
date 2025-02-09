# ex4
numbers_arr1 = [3,2,33,0]

for i in numbers_arr1:
  print(i)

numbers_arr2 = [1000,5,29,-5 ]

for j in numbers_arr2:
  print(j)

x = len(numbers_arr1)
print(x)

y = len(numbers_arr2)
print(y)

arrlength = len(numbers_arr1)


print("starting")
arr1_counter = 0
arr2_counter = 0

for i in range(0, arrlength):
    if numbers_arr1[i] > numbers_arr2[i]:
        arr1_counter += 1
    elif numbers_arr1[i] < numbers_arr2[i]:
        arr2_counter += 1
if arr1_counter > arr2_counter:
    print ("numbers_arr1 is the biggest" )
elif arr2_counter > arr1_counter:
    print ("numbers_arr2 is the biggest" )
