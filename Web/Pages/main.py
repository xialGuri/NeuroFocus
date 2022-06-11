f = open("./result.txt", 'w')
for i in range(0, 1):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()