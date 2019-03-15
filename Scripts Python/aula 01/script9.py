quadrados=[]

for i in range(1,11):
    quadrados.append(i*i)
print(quadrados)

quadrados=[i*i for i in range(1,11)]
print(quadrados)

quadrados=[i*i for i in range(1,11) if i%2 !=0]
print(quadrados)



