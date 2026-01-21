#create a dictionary
student={"roll_n0":14, "name":"janhavi","mark":85}
print(student)

#update dictionary
student["mark"]=90
student["grade"]="A"
print(student)
print()

#removing element
removed_value=student.pop("grade")
print(removed_value)
print(student)

#merging dictionary
dic2={"a":1,"b":2, "b":5}
merged_dictionary=student|dic2
print(merged_dictionary)