import os
import sys
import click
from rich.console import Console
from modfile_py_renamer.file_renamer import rename_files

console = Console()

@click.group()
def cli():
    """🎯 modfile-py-renamer: Una CLI sencilla para manejar archivos"""
    pass

@click.command()
@click.option('--directory', prompt='📁 Ingresa la ruta de la carpeta', help='Carpeta donde se encuentran los archivos.')
def renombrar(directory):
    """✏️  Renombrar archivos en una carpeta"""
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' no es un directorio válido.")
        sys.exit(1)

    console.print("[bold cyan]Comenzando a renombrar archivos...[/bold cyan]")
    rename_files(directory)
    console.print("[green]✔️  Proceso de renombrado completado.[/green]")

@click.command()
def salir():
    """👋 Salir de la aplicación CLI"""
    console.print("[bold red]Adiós, ¡vuelve pronto![/bold red] 👋")

cli.add_command(renombrar)
cli.add_command(salir)

if __name__ == '__main__':
    cli()
