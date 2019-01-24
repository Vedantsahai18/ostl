class Length:
    factor = {'millimetre': 0.001, 'centimetre': 0.01, 'metre': 1.0, 'kilometre': 1000., 'mile': 0.000621371,
              'foot': 3.28084, 'yard': 1.09361, 'inch': 39.3701}

    def __init__(self, in_value, unit):
        self.value = in_value
        self.unit = unit

    def convert(self, out_unit_):
        return Length(self.value * self.__class__.factor[out_unit_] / self.__class__.factor[self.unit], out_unit_)

    @classmethod
    def units(cls):
        return cls.factor.keys()


class Temperature:
    units_ = {'celsius', 'fahrenheit'}

    def __init__(self, in_value, unit):
        self.value = in_value
        self.unit = unit

    def convert(self, out_unit_):
        if self.unit == 'celsius' and out_unit_ == 'fahrenheit':
            return Temperature(self.value * 9 / 5 + 32, out_unit_)
        if self.unit == 'fahrenheit' and out_unit_ == 'celsius':
            return Temperature((self.value - 32) * 5 / 9, out_unit_)

    @classmethod
    def units(cls):
        return cls.units_


if __name__ == '__main__':
    in_unit = input("Enter incoming unit   : ")
    value = float(input("Enter incoming value  : "))
    out_unit = input("Enter outgoing unit   : ")
    incoming_measurement = None
    outgoing_measurement = None

    if in_unit in Length.units():
        incoming_measurement = Length(value, in_unit)
        outgoing_measurement = incoming_measurement.convert(out_unit)
    elif in_unit in Temperature.units():
        incoming_measurement = Temperature(value, in_unit)
        outgoing_measurement = incoming_measurement.convert(out_unit)

    print(incoming_measurement.value, incoming_measurement.unit, " = ", outgoing_measurement.value,
          outgoing_measurement.unit)
