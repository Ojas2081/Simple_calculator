import math


class Arithmetic:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        try:
            result = self.num1 + self.num2
        except Exception as e:
            return e
        return result

    def subtract(self):
        try:
            result = self.num1 - self.num2
        except Exception as e:
            return e
        return result

    def multiply(self):
        try:
            result = self.num1 * self.num2
        except Exception as e:
            return e
        return result

    def divide(self):
        try:
            result = self.num1 / self.num2
        except Exception as e:
            return e
        return result


class Trigonometry:
    def __init__(self, angle):
        self.angle = angle

    def sin_trig(self):
        return math.sin(self.angle)

    def cos_trig(self):
        return math.cos(self.angle)

    def tan_trig(self):
        return math.tan(self.angle)

    def cot_trig(self):
        return 1/math.tan(self.angle)

    def sec_trig(self):
        return 1/math.cos(self.angle)

    def cosec_trig(self):
        return 1/math.sin(self.angle)
