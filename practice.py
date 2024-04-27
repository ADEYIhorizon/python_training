import time

fruits = ["apple", "banana", "cherry", "kiwi", "mango", "apple", "banana", "cherry", "kiwi", "mango"
"apple", "banana", "cherry", "kiwi", "mango", "apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

start = time.time()
for x in fruits:
  if "a" in x:
    newlist.append(x)

# record end time
end = time.time()
 
# print the difference between start 
# and end time in milli. secs
# print("The time of execution of above program is :",  (end-start) * 10**6, "s")

# print(newlist)

# start = time.time()
# newlist1 = [x for x in fruits if "a" in x]
# end = time.time()
# print("The time of List Comprehension is :",  (end-start) * 10**6, "s")

old_number = [x for x in range(300) if x%2  == 0]
print(len(old_number))

for i, old_number in enumerate(old_number):
    print(i, old_number)

