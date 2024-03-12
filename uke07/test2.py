class Color:
    def __init__(self,rgb_value,name):
        self._rgb_value = rgb_value
        self._name = name
    
    @property
    def rgb_value(self):
        "This is the rgb_value property"
        return self._rgb_value
    
    @rgb_value.setter
    def rgb_value(self,newRgb_value):
        if newRgb_value>16777215 or newRgb_value<0:
            raise ValueError("Not an valid rgb number!")
        self._rgb_value = newRgb_value
    
    @property
    def name(self):
        return self._name
        
    
    @name.setter
    def name(self,newName):
        if not newName:
            raise ValueError("No name..")
        self._name = newName


if __name__ == "__main__":
    c = Color(0xff0000,"red")
    c.rgb_value = 100
    c.rgb_value = -2