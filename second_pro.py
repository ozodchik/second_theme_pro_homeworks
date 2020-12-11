import hashlib

def gener_ex(file_name):
    for i in file_name:
        my_hash = hashlib.md5(i)
        yield my_hash.hexdigest()


with open("C:/Users/озод/PycharmProjects/first/second_pro_homework/file.txt", "rb") as file:
    a = gener_ex(file)
    file.readline()
    for b in a:
        print(b)
