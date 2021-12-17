#!/usr/bin/env python
# coding: utf-8

# In[52]:


class PrimaryClass():
    def __init__(self, arg1, arg2):
        self.attr1=arg1
        self.attr2=arg2
        
    def printVal(self,arg3):
        print(f'Result of calculation is {(self.attr1+self.attr2)*arg3}')
        
primary= PrimaryClass(4,5)
primary.printVal(3)


# isinstance
if isinstance(primary, PrimaryClass):
    print("Object is instance of class")
else:
    print("No it is not instance")

#hasattr
at='attr1'    
if hasattr(primary, f'{at}'):
    print(f"Object has attribute {at} ")
    #getattr
    print(f'Attribute before {at} before editing has value {getattr(primary, at)}')
    primary.printVal(3)
    #setattr
    setattr(primary, at, 10)
    print(f'Attribute before {at} before editing has value {getattr(primary, at)}')
    primary.printVal(3)
else:
    print(f"There is not {at} atribute")
    print("And cant edit of attribute value which do not exists")
    primary.printVal(3)

    
    

# Inheritance
class SecondaryClass(PrimaryClass):
    def __init__ (self, sec_arg1, sec_arg2, arg1, arg2):
        PrimaryClass.__init__(self, arg1, arg2)
        self.sec_attr1=sec_arg1
        self.sec_attr2=sec_arg2
        
    def calcSecondary(self, param):
        print(f'Secondary only: {param*(self.sec_attr1+self.sec_attr2)}')
    def calcTotalValue(self, param):
        print(f'Total value: {((self.attr1+ self.attr2)*3)+param*(self.sec_attr1+self.sec_attr2)}')
    
        
secondaryObj=SecondaryClass(4,5,3,2)
print(secondaryObj.attr1)
print(secondaryObj.attr2)

secondaryObj.printVal(3)

secondaryObj.calcSecondary(2)

secondaryObj.calcTotalValue(2)


# In[ ]:




