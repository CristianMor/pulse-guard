import os
import glob

from rich import print
from tool.rename import rename

def verify_missing_data():

    rms_path = os.getenv('RMS_PATH')
    csv_path = os.getenv('CSV_PATH')

    # Verificar si las variables de entorno están configuradas
    if not rms_path or not csv_path:
        print("[red]Error: Las variables de entorno RMS_PATH y CSV_PATH deben estar configuradas.[/red]")
        return
    
    # Obtener todos los archivos _Rms_upd.txt en la ruta rms
    txt_files = glob.glob(os.path.join(rms_path, '*Rms*_upd.txt'))

    txt_files_total = len(txt_files)
    files_to_rename = []
    missing_file_total = 0

    for file in txt_files:
        # Obtener el nombre base del archivo .txt
        base_name = os.path.splitext(os.path.basename(file))[0]

        # Construir el nombre esperado del archivo .csv
        csv_name = base_name.replace('Rms_upd', 'Data') + '.csv'
        csv_complete_path = os.path.join(csv_path + base_name[:3] + '/', csv_name)

        # Verificar si el archivo .csv existe
        if not os.path.exists(csv_complete_path):
            files_to_rename.append(f"{base_name}.txt")
            missing_file_total = missing_file_total + 1
            print(f"[red]Faltante: {csv_name}[/red] - [bold yellow]Sonido: {base_name}.txt[/bold yellow]")


    print(f"{missing_file_total} [green]archivos de data faltantes de [/green]{txt_files_total} [green]archivos de sonido procesados.[/green]")

    # if missing_file_total > 0:
    #     print("Mostramos la funcion de corregir")

    return

