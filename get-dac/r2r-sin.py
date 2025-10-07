import r2r_dac as r2r
import signal_generator as sg
import time

# Параметры генерируемого сигнала
amplitude = 3.2          # Амплитуда сигнала в Вольтах
signal_frequency = 10    # Частота сигнала в Гц
sampling_frequency = 1000  # Частота дискретизации в Гц

try:
    # Создаем объект для управления R2R ЦАП
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)
    
    print(f"Генерация синусоидального сигнала:")
    print(f"Амплитуда: {amplitude} В")
    print(f"Частота сигнала: {signal_frequency} Гц")
    print(f"Частота дискретизации: {sampling_frequency} Гц")
    print("Для остановки нажмите Ctrl+C")
    
    start_time = time.time()
    
    # Бесконечный цикл генерации сигнала
    while True:
        # Вычисляем текущее время относительно начала генерации
        current_time = time.time() - start_time
        
        # Получаем нормализованную амплитуду сигнала
        normalized_amp = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        
        # Вычисляем напряжение для текущей точки сигнала
        voltage = normalized_amp * amplitude
        
        # Подаем напряжение на ЦАП
        dac.set_voltage(voltage)
        
        # Ждем до следующего периода дискретизации
        sg.wait_for_sampling_period(sampling_frequency)

except KeyboardInterrupt:
    print("\nГенерация сигнала остановлена")

finally:
    # Корректно завершаем работу с ЦАП
    dac.deinit()
    print("ЦАП отключен")