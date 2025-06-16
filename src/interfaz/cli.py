# src/interfaz/cli.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from modelos.clinica import Clinica
from modelos.excepciones import (
    PacienteNoEncontradoError,
    MedicoNoEncontradoError,
    EspecialidadNoEncontradaError,
    TurnoExistenteError
)

class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        print("\n--- Menú Clínica ---")
        print("1) Agregar paciente")
        print("2) Agregar médico")
        print("3) Agendar turno")
        print("4) Agregar especialidad a médico")
        print("5) Emitir receta")
        print("6) Ver historia clínica")
        print("7) Ver todos los turnos")
        print("8) Ver todos los pacientes")
        print("9) Ver todos los médicos")
        print("0) Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.agregar_medico()
            elif opcion == "3":
                self.agendar_turno()
            elif opcion == "4":
                self.agregar_especialidad_medico()
            elif opcion == "5":
                self.emitir_receta()
            elif opcion == "6":
                self.ver_historia_clinica()
            elif opcion == "7":
                self.ver_todos_los_turnos()
            elif opcion == "8":
                self.ver_todos_los_pacientes()
            elif opcion == "9":
                self.ver_todos_los_medicos()
            elif opcion == "0":
                print("Saliendo...")
                break
            else:
                print("Opción inválida, intente nuevamente.")

    def agregar_paciente(self):
        try:
            nombre = input("Nombre del paciente: ").strip()
            dni = input("DNI del paciente: ").strip()
            fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ").strip()
            self.clinica.agregar_paciente(nombre, dni, fecha_nac)
            print("Paciente agregado correctamente.")
        except Exception as e:
            print(f"Error: {e}")

    def agregar_medico(self):
        try:
            nombre = input("Nombre del médico: ").strip()
            matricula = input("Matrícula del médico: ").strip()
            especialidades = {}
            while True:
                esp = input("Especialidad (dejar vacío para terminar): ").strip()
                if esp == "":
                    break
                dias = input(f"Días de atención para {esp} (separados por coma): ").strip()
                dias_lista = [d.strip() for d in dias.split(",") if d.strip()]
                especialidades[esp] = dias_lista
            self.clinica.agregar_medico(nombre, matricula, especialidades)
            print("Médico agregado correctamente.")
        except Exception as e:
            print(f"Error: {e}")

    def agendar_turno(self):
        try:
            dni_paciente = input("DNI del paciente: ").strip()
            matricula_medico = input("Matrícula del médico: ").strip()
            especialidad = input("Especialidad: ").strip()
            fecha_hora = input("Fecha y hora (YYYY-MM-DD HH:MM): ").strip()
            self.clinica.agendar_turno(dni_paciente, matricula_medico, especialidad, fecha_hora)
            print("Turno agendado correctamente.")
        except (PacienteNoEncontradoError, MedicoNoEncontradoError, EspecialidadNoEncontradaError, TurnoExistenteError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def agregar_especialidad_medico(self):
        try:
            matricula = input("Matrícula del médico: ").strip()
            esp = input("Especialidad a agregar: ").strip()
            dias = input("Días de atención (separados por coma): ").strip()
            dias_lista = [d.strip() for d in dias.split(",") if d.strip()]
            self.clinica.agregar_especialidad_medico(matricula, esp, dias_lista)
            print("Especialidad agregada correctamente.")
        except (MedicoNoEncontradoError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def emitir_receta(self):
        try:
            dni_paciente = input("DNI del paciente: ").strip()
            matricula_medico = input("Matrícula del médico: ").strip()
            medicamentos = []
            print("Ingrese los medicamentos (deje vacío para terminar):")
            while True:
                med = input("- ").strip()
                if med == "":
                    break
                medicamentos.append(med)
            self.clinica.emitir_receta(dni_paciente, matricula_medico, medicamentos)
            print("Receta emitida correctamente.")
        except (PacienteNoEncontradoError, MedicoNoEncontradoError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def ver_historia_clinica(self):
        try:
            dni = input("DNI del paciente: ").strip()
            historia = self.clinica.ver_historia_clinica(dni)
            print("=== Historia Clínica ===")
            print(historia)
        except PacienteNoEncontradoError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def ver_todos_los_turnos(self):
        turnos = self.clinica.ver_todos_los_turnos()
        if turnos:
            print("=== Turnos ===")
            for t in turnos:
                print(t)
        else:
            print("No hay turnos registrados.")

    def ver_todos_los_pacientes(self):
        pacientes = self.clinica.ver_todos_los_pacientes()
        if pacientes:
            print("=== Pacientes ===")
            for p in pacientes:
                print(p)
        else:
            print("No hay pacientes registrados.")

    def ver_todos_los_medicos(self):
        medicos = self.clinica.ver_todos_los_medicos()
        if medicos:
            print("=== Médicos ===")
            for m in medicos:
                print(m)
        else:
            print("No hay médicos registrados.")

if __name__ == "__main__":
    cli = CLI()
    cli.ejecutar()
