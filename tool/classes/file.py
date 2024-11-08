import os
import glob
import datetime

class File:

    def getFilesRmsUpdToday():

        rms_path = os.getenv('RMS_PATH')
        today = datetime.date.today().strftime('%Y-%m-%d').split('-')
        [year, month, day] =  today
        pattern = f"*{day}{month}*{year[-2:]}*Rms*_upd.txt"

        # Obtener todos los archivos de hoy _Rms_upd.txt en la ruta rms
        today_files = glob.glob(os.path.join(rms_path, pattern))
        return today_files
