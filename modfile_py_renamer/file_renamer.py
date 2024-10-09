import os
import sys
import re
from rich import print

def rename_files(directory):

    pattern = re.compile(r"(\d{3})_(\d{10})_(.*?)_upd\.txt")

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            match = pattern.match(filename)
            if match:
                # Tomando los primeros 8 dígitos del segundo grupo (10 dígitos)
                new_name = f"{match.group(1)}_{match.group(2)[:8]}_{match.group(3)}.txt"

                if new_name != filename:
                    old_path = os.path.join(directory, filename)
                    new_path = os.path.join(directory, new_name)
                    try:
                        os.rename(old_path, new_name)
                        print(f"[green]Renombrado exitoso:[/green] {filename} -> [bold yellow]{new_name}[/bold yellow]")
                    except Exception as e:
                        print(f"[red]Error al renombrar:[/red] {str(e)}")
                else:
                    print(f"[blue]Sin cambios:[/blue] {filename}")
            else:
                print(f"[red]No coincide con el patrón:[/red] {filename}")
