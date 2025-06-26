# Types Of Methods
# static class instance
# self -> object
# cls -> class

class Methods:
    cname = "Zensar"
    name = "Sumit"

    def instance_method(self):
        print("this is instance method")

    @classmethod
    def class_method(cls):
        print("this is class method")
        cls.cname = "Oracle"

    @staticmethod
    def static_method():
        print("this is static method")

    @classmethod
    def class_method_param(cls, name):
        cls.name = name
        return "this is param class method " + name

print(Methods.name)
print(Methods.class_method_param("Sakshi"))
print(Methods.name)
print(Methods.cname)
Methods.class_method()
print(Methods.cname)
Methods.static_method()

m1 = Methods()
m1.instance_method()