import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose


        GPIO.setmode(GPIO.BCM)
        pwm = GPIO.PWM(self.gpio_pin, pwm_frequency)
        pwm.start(0)
        

    def denit():
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        



if __name__ == '__main__':
    try:
        dac = R2R_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число: Попробуйте еще раз\n")

    finally:
        dac.deinit()
        