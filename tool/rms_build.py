import os
import numpy as np
import soundfile as sf

from tool.classes.file import File
from scipy.signal import butter, filtfilt

'''
    Centrar los datos y normalizarlos al rango [-1, 1].
    Si los datos tiene poca variabilidad o si el valor máximo es 0, evitar errores al normalizar.
'''
def normalize_and_center_data(data):
    # Si los datos tiene poca variabilidad, evitar la normalización
    if np.std(data) < 1e-10:
        print("Advertencia: Normalización omitida por poca variabilidad.")
        return data - np.mean(data)

    # Centrar datos restando la media
    data = data - np.mean(data)
    max_abs = np.max(np.abs(data))

    # Normalizar datos al rango [-1, 1] si el valor máximo es mayor a 0
    if max_abs > 0:
        data = data / max_abs
    else: 
        print("Advertencia: Valor máximo absoluto es 0 durante la normalización.")
        data = np.zeros_like(data)  # Devolvemos ceros para evitar NaN

    return data

'''
    Generar un onda sinusoidal con una frecuencia específica.
    Como señal portadora para la modulación.
'''
def generate_sine_wave(frequency, duration, sample_rate=44100):
    # Crea un array de tiempo
    t = np.linspace(0, duration, int(sample_rate * duration))
    # Generar onda sinusoidal
    return np.sin(2 * np.pi * frequency * t)

'''
    Crear un filtro pasa-banda usando el filtro Butterworth.
'''
def butter_bandpass(lowcut, highcut, fs, order=3):
    nyquist = 0.5 * fs  # Frecuencia de Nyquist
    low = lowcut / nyquist
    high = highcut / nyquist
    # Calcular coeficientes del filtro
    b, a = butter(order, [low, high], btype='band')
    return b, a

'''
    Aplicar un filtro pasa-banda a los datos para aislar ciertas frecuencias.
'''
def apply_bandpass_filter(data, lowcut, highcut, fs, order=3):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)

    # Verificar variabilidad de los datos
    if np.std(data) < 1e-10:
        print("Advertencia: Datos contienen NaN o Inf antes del filtrado.")
        return np.zeros_like(data)
    
    try:
        # Aplicar filtro pasa-banda
        filtered_data = filtfilt(b, a, data)
    except ValueError as e:
        print(f"Error al aplicar filtro: {e}")
        return np.zeros_like(data)

    # Manejo de datos NaN
    if np.any(np.isnan(filtered_data)):
        print("Error: Datos contienen NaN después del filtrado.")
        return np.zeros_like(data)

    return filtered_data

'''
    Procesar los datos RMS para generar una señal de audio modulada y filtrada.
'''
def process_audio_data(audio_data, sample_rate, frequency=440):
    # Normalizar y centrar datos de audio
    audio_data = normalize_and_center_data(audio_data)
    duration = len(audio_data) / sample_rate
    
    # Generar onda portadora
    carrier = generate_sine_wave(frequency, duration, sample_rate)

    # Modulación de amplitud
    modulated_audio = carrier * audio_data
    modulated_audio = normalize_and_center_data(modulated_audio)

    # Filtro y mezcla de bandas
    low_band = apply_bandpass_filter(modulated_audio, 50, 500, sample_rate) * 1.5
    mid_band = apply_bandpass_filter(modulated_audio, 500, 2000, sample_rate) * 1.8
    high_band = apply_bandpass_filter(modulated_audio, 2000, 5000, sample_rate) * 0.8
    processed_audio = low_band + mid_band + high_band

    # Normalizar audio procesado
    processed_audio = normalize_and_center_data(processed_audio)
    processed_audio *= 2.0 # Incrementar amplitud para mejorar audibilidad

    print(f"Rango del audio procesado: Min={np.min(processed_audio):.2f}, Max={np.max(processed_audio):.2f}")
    return processed_audio

'''
    Ajustar los datos RMS al número de muestras requerido para la duración deseada del audio.
'''
def interpolate_audio(rms_data, target_sample_rate=44100, target_duration=300):
    total_samples = int(target_sample_rate * target_duration)
    t_original = np.linspace(0, target_duration, len(rms_data))
    t_interpolated = np.linspace(0, target_duration, total_samples)
    interpolated_rms = np.interp(t_interpolated, t_original, rms_data)
    return interpolated_rms 

'''
    Leer y normalizar los datos RMS desde un archivo .txt.
'''
def extract_rms_data(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    content = content.replace('[', '').replace(']', '')

    try:
        values = [float(x.strip()) for x in content.split(',') if x.strip()]
        values = np.array(values)
        # Normalización al rango [-1, 1]
        min_value, max_value = np.min(values), np.max(values)
        values = 2 * ((values - min_value) / (max_value - min_value)) - 1

        print(f"Datos RMS normalizados: Min={np.min(values):.2f}, Max={np.max(values):.2f}")
        return values
    except ValueError as e:
        print(f"Error al procesar el archivo {rms_file}: {e}")
        return None

'''
    Generar y guardar el archivo de audio .wav con fade-in y fade-out.
'''
def save_rms_to_wav(file_path, frequency=440, target_duration=300):
    wav_dir = 'wav'
    if not os.path.exists(wav_dir):
        os.makedirs(wav_dir)
    
    rms_data = extract_rms_data(file_path)
    if rms_data is None or len(rms_data) == 0:
        print(f"No se pudieron extraer los datos válidos del archivo {file_path}")
        return
    
    sample_rate = 44100 
    audio_data = interpolate_audio(rms_data, sample_rate, target_duration)
    audio_data = process_audio_data(audio_data, sample_rate, frequency)

    # Aplicar fade-in y fade-out
    fade_samples = int(sample_rate * 2) # 2 seconds for fade
    envelope = np.ones_like(audio_data)
    envelope[:fade_samples] = np.linspace(0, 1, fade_samples) 
    envelope[-fade_samples:] = np.linspace(1, 0, fade_samples) 
    audio_data *= envelope

    # make name to file output
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    iddisp_dir = f'wav/{base_name[:3]}'

    if not os.path.exists(iddisp_dir):
        os.makedirs(iddisp_dir)

    wav_file = os.path.join(iddisp_dir, f"{base_name}.wav")

    # save file wav
    sf.write(wav_file, audio_data, sample_rate)
    print(f"Archivo de audio guardado: {wav_file}")
    print(f"Duración del audio: {len(audio_data)/sample_rate:.2f} segundos")

'''
    Procesar archivos RMS actuales y generar archivos de audio.
'''
def rms_build():
    today_files = File.getFilesRmsUpdToday()
    print(f"{len(today_files)} archivos para procesar")

    for rms_file in today_files:
        save_rms_to_wav(rms_file, frequency=880)
