# File(txt, json, excel) Handling(Operations -> read, write, close, open)

class Students_of_ndmvp:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + str(self.age)

s1 = Students_of_ndmvp('Yash', 25)
# s2 = Students_of_ndmvp('Sumit', 20)

# list_of_stds = [s1, s2]
# object to byte -> Serialization

# load()  -> read(), dump() -> write()
f1 = open("data.txt","wb")

import pickle
pickle.dump(s1, f1)

f1.close()

f1_read = open("data.txt","rb")
print(pickle.load(f1_read))