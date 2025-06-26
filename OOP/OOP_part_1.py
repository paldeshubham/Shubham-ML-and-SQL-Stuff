class Temp:
    def __init__(self):
        print("hello")
obj = Temp()

#methods vs Functions: whatever functions that are present inside the class are known as Methods , whereas all outside the class are called as functions.

#why to use constructor (interview question) : the things whose controls you dont wanna give to the user usko hi hum constructor ke andar likhte hai. means jab hame control users ke paas dena hota hai tab hum noraml methods ka use karte hai , lekin jab hume control user ko nahi dena hai jab application start ho tab hum constructor ka use karenge .constructor are used to write configuration related code.

#you cannot change the name of the constructor.



#Concept of self: jitne bhi apne methods banaye unme self ek deafault parameter hai.
# 2 . constructor ke andar jitne bhi parameter banaye wo saare self se initialize kiye hai
# 3. jab bhi method ko call kar rahe ko constructor kw andar tab bhi hum self ka hi use karte hai 

'''
lekin ye self hai kya: 

golder rule of oop: so oop mai 2 dije hoti hai class and object 

class ke andar hum rula banate hai jo object follow karta hai

aap ke class ke andar jo member hai wo sirf or sirf  class ka object hi access kar sakta hai. khudke class ke methods bhi dusre methods ko access nhi kar sakte.

so self aur koi nahi apka object hi hai.

self is the current object.

aur naam sirf self hi hona jaruri nahi hai hum use kuch bhi naam de sakte hai like salman khan , sharkhukh khan etc.
'''
class Temp:
    def __init__(self):
        print(id(self))
        print("hello")
        self.hello()

    def hello(self):
        print("This is hello method")
obj = Temp()
print(id(obj))

#obj ka id aur self ka id same hai . so uske wajah se ham 