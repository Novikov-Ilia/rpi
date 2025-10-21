import numpy as np
import time

def get_sin_wave_amplitude(freq, time_point):
    """
    Вычисляет амплитуду синусоидального сигнала в заданный момент времени
    
    Args:
        freq: частота сигнала в Гц
        time_point: момент времени в секундах
    
    Returns:
        Нормализованная амплитуда от 0 до 1
    """
    # Вычисляем значение синуса: sin(2πft)
    sin_value = np.sin(2 * np.pi * freq * time_point)
    
    # Сдвигаем от [-1, 1] к [0, 2] и нормализуем к [0, 1]
    normalized_amplitude = (sin_value + 1) / 2
    
    return normalized_amplitude

def wait_for_sampling_period(sampling_frequency):
    """
    Ожидает один период дискретизации
    
    Args:
        sampling_frequency: частота дискретизации в Гц
    """
    sampling_period = 1.0 / sampling_frequency
    time.sleep(sampling_period)


def get_triangle_wave_amplitude(freq,current_time):
    period = 1.0/ freq
    phase = current_time % period / period

    return 2 * min (phase, 1 - phase)