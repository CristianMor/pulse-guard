import os
import numpy as np
import soundfile as sf

from tool.classes.file import File

def interpolate_audio(rms_data, target_sample_rate=44100, target_duration=300):
    total_samples = int(target_sample_rate * target_duration)

    t_original = np.linspace(0, target_duration, len(rms_data))

    t_interpolated = np.linspace(0, target_duration, total_samples)

    interpolated_rms = np.interp(t_interpolated, t_original, rms_data)

    return interpolated_rms 

def extract_rms_data(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # eliminate characters '[' y ']' if exists
    content = content.replace('[', '').replace(']', '')

    try:
        values = [float(x.strip()) for x in content.split(',') if x.strip()]
        return np.array(values)
    except ValueError as e:
        print(f"Error al procesar el archivo {rms_file}: {e}")
        return None

def save_rms_to_wav(file_path, frequency=440, target_duration=300):

    # make directory 'wav' if not exists
    wav_dir = 'wav'
    if not os.path.exists(wav_dir):
        os.makedirs(wav_dir)
    
    rms_data = extract_rms_data(file_path)

    if rms_data is None or len(rms_data) == 0:
        print(f"No se pudieron extraer los datos válidos del archivo {file_path}")
        return
    
    sample_rate = 44100

    print(f"Datos RMS extraidos: {len(rms_data)} valores")
    print(f"Rango de valores: min={np.min(rms_data):.2f}, max={np.max(rms_data):.2f}")

    audio_data = interpolate_audio(rms_data, sample_rate, target_duration)

    # normalize data RMS to range [-1, 1]
    audio_data = audio_data / np.max(np.abs(audio_data))

    # apply fade-in and fade-out 
    fade_duration = int(sample_rate * 0.1) # 0.1 seconds for fade
    fade_in = np.linspace(0, 1, fade_duration)
    fade_out = np.linspace(1, 0, fade_duration)

    audio_data[:fade_duration] *= fade_in
    audio_data[-fade_duration:] *= fade_out

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

def rms_build():

    today_files = File.getFilesRmsUpdToday()
    # proccesing each file data rms
    for rms_file in today_files:
        save_rms_to_wav(rms_file, frequency=880)
