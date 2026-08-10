n=input("Enter last few days temperature in °C:").split(",")
l=[int(item) for item in n]

sum=0
for i in range(0,len(l)):
    sum += l[i]

Avg_temprature = sum / len(l)

print("Your area Average Temprature is:",int(Avg_temprature),"°C")
