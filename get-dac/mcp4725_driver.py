import smbus

class MCP4725:

    def __init__(self, dynamic_range, addres=0x61, verbose=True):
        self.bus = smbus.SMBus(1)

        self.addres = addres
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print(number)
            print("На вход можно подавать только целые числа")
            return

        if not 0 <= number <=4095:
            print("Число выходит за разрядность MCP4725 (12 бит)")
            return

        first_byte = self.wm | self.pds | (number >> 8)
        second_byte = number & 0xFF
        self.bus.write_byte_data(self.addres, first_byte, second_byte)

    def set_voltage(self, voltage):
        if not (0 <= voltage <= self.dynamic_range):
            print("Число выходит за динамический диапазон")
            return

        voltage_12b = (voltage/self.dynamic_range)*3810

        self.set_number(int(voltage_12b))

            


if __name__ == '__main__':
    try:
        mcp = MCP4725(4.8)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                mcp.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число: Попробуйте еще раз\n")

    finally:
        mcp.deinit()
        