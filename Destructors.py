# when the object self destroyed it is called destructors
#  __del__() it is the  only one destruction method
class employee:
    def __init__(self):
        print("employee.")
    def __del__(self):
        print("destruction called ,employee deleted.")
e=employee()
del e
#e
