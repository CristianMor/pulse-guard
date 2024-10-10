import os
import re
from rich import print 

def rename():

    rms_path = os.getenv('RMS_PATH')

    if not os.path.isdir(rms_path):
        console.print(f"[bold red]Error: '{rms_path}' no es un directorio válido.[/bold red]")
        sys.exit(1)

    pattern = re.compile(r"(\d{3})_(\d{10})_(.*?)_upd\.txt")

    files = os.listdir(rms_path)

    rename_files_total = 0
    upd_files_total = len(files)

    for file in files:
        if file.endswith(".txt"):
            match = pattern.match(file)

            if match:
                # Tomando los primeros 8 dígitos del segundo grupo (10 dígitos)
                new_file = f"{match.group(1)}_{match.group(2)[:8]}_{match.group(3)}.txt"

                if new_file != file:
                    old_path = os.path.join(rms_path, file)
                    new_path = os.path.join(rms_path, new_file)

                    try:
                        os.rename(old_path, new_path)
                        rename_files_total = rename_files_total + 1
                        print(f"[green]Renombrado exitoso:[/green] {file} -> [bold yellow]{new_file}[/bold yellow]")
                    except Exception as e:
                        print(f"[red]Error al renombrar: [/red] {str(e)}")
                else:
                    print(f"[blue]Sin cambios: [/blue] {file}")


    print(f"{rename_files_total} [green]archivos renombrados de [/green]{upd_files_total} [green]archivos de sonido verificados.[/green]")
