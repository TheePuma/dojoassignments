# def oddeven():
# 	for i in range (0,2000):
# 		if i % 2 == 0:
# 			print("number is ", i,". This is an even number")
# 		else:
# 			print("number is ", i,". This is an odd number")
# print (oddeven())
def multiply(arr, num):
	for x in range (0,len(arr)):
		arr[x] *= num
	return (arr)
# a=[2,4,10,16]
# print(multiply(a,5))
def layered_multiples(arr):
    print (arr)
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],2))
print (x)
