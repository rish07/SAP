data1 = ['music','tv','fan','light']
data2 = ['on','off']

text = input()

temp = text.split()

for i in temp:
    for j in data1:
        if i == j:
            for k in temp:
                if k == data2[0]:
                    print(j,data2[0])
                if k == data2[1]:
                    print(j, data2[1])