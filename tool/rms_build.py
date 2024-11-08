import os
import numpy as np
import soundfile as sf

from tool.classes.file import File

def rms_to_audio(rms_data, sample_rate=44100, frequency=440):
    # Normalize data RMS to range [-1, 1]
    audio_data = 2 * ((rms_data - np.min(rms_data)) / (np.max(rms_data) - np.min(rms_data))) - 1

    # Generate signal audio
    duration = len(audio_data) / sample_rate
    t = np.linspace(0, duration, len(audio_data))
    audio = audio_data * np.sin(2 * np.pi * frequency * t)
    return audio

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

def save_rms_to_wav(file_path, sample_rate=441000, frequency=440):

    # make directory 'wav' if not exists
    wav_dir = 'wav'
    if not os.path.exists(wav_dir):
        os.makedirs(wav_dir)
    
    rms_data = extract_rms_data(file_path)

    if rms_data is None or len(rms_data) == 0:
        print(f"No se pudieron extraer los datos válidos del archivo {file_path}")
        return
    
    print(f"Datos RMS extraidos: {len(rms_data)} valores")
    print(f"Rango de valores: min={np.min(rms_data):.2f}, max={np.max(rms_data):.2f}")

    audio = rms_to_audio(rms_data)

    # ensure duration audio
    if len(audio) < sample_rate:
        repetitions = int(np.ceil(sample_rate / len(audio)))
        audio = np.tile(audio, repetitions)

    # make name to file output
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    iddisp_dir = f'wav/{base_name[:3]}'

    if not os.path.exists(iddisp_dir):
        os.makedirs(iddisp_dir)

    wav_file = os.path.join(iddisp_dir, f"{base_name}.wav")

    # save file wav
    sf.write(wav_file, audio, sample_rate)
    print(f"Archivo de audio guardado: {wav_file}")
    print(f"Duración del audio: {len(audio)/sample_rate:.2f} segundos")

def rms_build():

    today_files = File.getFilesRmsUpdToday()
    # proccesing each file data rms
    for rms_file in today_files:
        save_rms_to_wav(rms_file, frequency=880)
