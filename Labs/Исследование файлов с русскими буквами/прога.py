file = open('Testtext.txt', 'rb')
#print(file.read())
print(file.read().decode('utf-8'))
'''for i in file:
    print(i.decode('utf-8'))'''
file.close()
'''array = [1,2,1,3,1,4,1,5,1]
i = array.index(1,3,5)
print(i)
print(array[i])'''
