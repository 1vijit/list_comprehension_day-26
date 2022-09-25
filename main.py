numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num*num for num in numbers]
print(squared_numbers)

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
resul = [num for num in list1 if num%2==0 ]
print(resul)

one = open("file1.txt", "r")
two = open("file2.txt", "r")
content_one = one.read()
list_o = content_one.split("\n")
content_two = two.read()
list_t = content_two.split("\n")

list_f = [seg1 for seg1 in list_o if seg1 in list_t]
print(list_o)
print(list_t)
print(list_f)