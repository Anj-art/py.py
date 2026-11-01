# q
''
'''
add = lambda a,b : a + b
print("sum = ",add (90,70))
'''
# q
''
'''
Average = lambda a,b: (a + b ) /2
print("Average = ",Average(27,33))
'''
# q 3
''
'''
maximum = lambda a,b: a if a > b else b
print(maximum(90,80))
'''
# q 4 sorted student according marks
''
'''
student = [
    ("anjali",98),
    ("jiya",89)
    ]
result = sorted(student,key = lambda x :x [1])
print(result)
'''
# q filter all even numbers
''
'''
dataset = [56,7,19,54,40]
even_number = list(filter(lambda x: x % 2 == 0, dataset))
print(even_number)
'''
# q filter ALL ODD NUMBER
''
'''
dataset = [34,44444,3553,54443,43,45,46]
even_number = list(filter (lambda x :x %2 == 0 ,dataset))
print(even_number)
'''
