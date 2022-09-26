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
# print(list_o)
# print(list_t)
# print(list_f)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?as"

result = {word:int(len(word)) for word in sentence.split(" ")}
# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:((temp_c * 9/5)+32) for (day,temp_c) in weather_c.items()}
print(weather_f)

import pandas
student_dict = {"student":["Angela", "James", "Lily"], "score": [56, 76, 98]}
student_data_frame = pandas.DataFrame(student_dict)
for (index,row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)


