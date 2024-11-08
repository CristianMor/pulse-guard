
import os
import sys
import click
import inquirer
import time

from rich.console import Console
from dotenv import load_dotenv
from tool.rename import rename 
from tool.verify_missing_data import verify_missing_data 
from tool.rms_build import rms_build

load_dotenv()
console = Console()

MENU_OPTIONS = {
    'Preparar Archivos para Reproceso': None,
    'Verificar data faltante': None,
    'Generar audio de hoy': None,
    # 'Corregir problemas': ('fix_issues', 'Selecciona el tipo de problema', ['missing_data', 'corrupt_data']),
    'Salir': None
}

def clear_screen():
    """Limpia la pantalla de la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(message, choices=None):
    """Obtiene la entrada del usuario."""
    if choices:
        question = [inquirer.List('response', message=message, choices=choices)]
    else:
        question = [inquirer.Text('response', message=message)]

    return inquirer.prompt(question)['response']

def handle_action(action, prompt=None, choices=None):
    """Maneja la acción seleccionada por el usuario."""
    clear_screen()
    
    arg = get_user_input(prompt, choices)
    globals()[action](arg)

@click.group()
def cli():
    """🔧 Herramienta CLI para monitorear y corregir archivos para el correcto funcionamiento del sistema."""
    pass


@click.command()
def verify_data():
    """🕵️‍♂️  Verificar data de sonido faltante """

    console.print("[bold cyan]Comenzando a verificar la data faltante...[/bold cyan]")
    verify_missing_data()
    console.print("[green]Proceso de verificar completado.[/green]")

@click.command()
def rename_to_recode():
    """✏️  Renombrar archivos RMS para volver a decodificar su información"""

    console.print("[bold cyan]Comenzando a renombrar archivos...[/bold cyan]")
    rename()
    console.print("[green]Proceso de renombrado completado.[/green]")
        
# Comando interactivo que da a los usuarios la opción de qué hacer
@click.command()
def interactive():
    """🤖 Menú interactivo para verificar y corregir archivos."""
    while True:
        clear_screen()
        click.echo("🎉🔊 Bienvenido a la herramienta de monitoreo de archivos de sonido 🍤")

        action = get_user_input(
            "¿Qué es lo que quieres realizar?",
            choices=list(MENU_OPTIONS)
        )

        if action == "Salir":
            clear_screen()
            console.print("[bold red]👋 Saliendo de la herramienta...[/bold red]")
            break

        if action == "Preparar Archivos para Reproceso":
            clear_screen()

            console.print("[bold cyan]Comenzando a renombrar archivos...[/bold cyan]")
            rename()
            console.print("[green]Proceso de renombrado completado.[/green]")
            break

        if action == "Verificar data faltante":
            clear_screen()
            console.print("[bold cyan]Comenzando a verificar la data faltante...[/bold cyan]")
            verify_missing_data()
            console.print("[green]Proceso de verificar completado.[/green]")
            break


        handle_action(*MENU_OPTIONS[action])

        input("\nPresiona Enter para continuar...")
 

@click.command()
def rms_to_audio():
    """✏️  Renombrar archivos RMS para volver a decodificar su información"""

    console.print("[bold cyan]Comenzando a renombrar archivos...[/bold cyan]")
    rms_build()
    console.print("[green]Proceso de renombrado completado.[/green]")

 # Agregando comandos
cli.add_command(verify_data)
cli.add_command(rename_to_recode)
cli.add_command(interactive)
cli.add_command(rms_to_audio)

# Entrada
def main():
    cli()

if __name__ == '__main__':
    main()
