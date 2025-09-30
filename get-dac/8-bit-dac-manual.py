import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

r2r = [16, 20, 21, 25, 26, 17, 27, 22]

GPIO.setup(r2r, GPIO.OUT)
dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит на динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В")
        print("Устанавливаем 0.0 В")
        return 0
    
    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    nbin = [ int(element) for element in bin(number)[2:].zfill(8) ]
    for i in range(len(nbin)):
        GPIO.output(r2r[i], nbin[i])

try:
    while True:
        try:
            voltage = float(input('Введите напряжеие в Вольтах:'))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        
        except ValueError:
            print('Вы ввели не число: Попробуйте еще раз\n')

finally:
    GPIO.output(r2r, 0)
    GPIO.cleanup()