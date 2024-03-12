
class Kaffemaskin:

    def __init__(self, max_vol):
        self._max_vol = max_vol
        self._curr_vol = 0

    @property
    def curr_vol(self):
        return self._curr_vol
    
    @curr_vol.setter
    def curr_vol(self, new_value):
        if new_value > self._max_vol:
            raise ValueError("Kaffemaskina blir overfylt")
        self._curr_vol = new_value

    def fyll(self, mengde):
        if mengde + self._curr_vol < self._max_vol:
            self._curr_vol += mengde
        else:
            self._curr_vol = self._max_vol

    def lag_espresso(self):
        if self._curr_vol >= 40:
            self._curr_vol -= 40
            return 40
        raise ValueError("Ikke nok vann i maskina")
    
    def __str__(self):
        return "Kaffemaskin maksvol: " + str(self._max_vol) + " currvol: " + str(self._curr_vol)
    

if __name__ == "__main__":
    kaffe1 = Kaffemaskin(200)
    kaffe1.fyll(200)
    print(kaffe1)
    kaffe1.lag_espresso()
    kaffe1.curr_vol = 1000000000000
    print(kaffe1)