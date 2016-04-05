

class Person():
    
    def __init__(self,name,adress,tel_num):
        self.__name = name
        self.__adress = adress
        self.__number = tel_num
        
        
    
        
        
class Qustomer(Person):
    
    def __init__(self,name,adress,tel,qus_num,data):
        Person.__init__(self, name, adress, tel_num)    
        self.num = qus_num
        self.data = data