
def CalAver(number):
    total = 0
    average = 0
    for i in number:
        total +=i
    average =(int)(total/len(number))
    return total,average

x=[87,45,33,72,87,92,88,76]
y,z = CalAver(x)
print(y)
print("Result :",z)
