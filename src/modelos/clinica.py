# clinica.py

from paciente import Paciente
from medico import Medico
from turno import Turno
from historia_clinica import HistoriaClinica
from excepciones import (
    PacienteYaExisteError, PacienteNoEncontradoError,
    MedicoYaExisteError, MedicoNoEncontradoError,
    TurnoYaExisteError, TurnoNoEncontradoError,
    HistoriaClinicaNoEncontradaError
)

class Clinica:
    def __init__(self):
        self.__pacientes = {}
        self.__medicos = {}
        self.__turnos = []
        self.__historias_clinicas = {}

    # Pacientes
    def agregar_paciente(self, paciente: Paciente):
        if paciente.dni in self.__pacientes:
            raise PacienteYaExisteError(f"Paciente con DNI {paciente.dni} ya existe.")
        self.__pacientes[paciente.dni] = paciente
        self.__historias_clinicas[paciente.dni] = HistoriaClinica(paciente)

    def obtener_paciente(self, dni: str) -> Paciente:
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoError(f"Paciente con DNI {dni} no encontrado.")
        return self.__pacientes[dni]

    # Médicos
    def agregar_medico(self, medico: Medico):
        if medico.matricula in self.__medicos:
            raise MedicoYaExisteError(f"Médico con matrícula {medico.matricula} ya existe.")
        self.__medicos[medico.matricula] = medico

    def obtener_medico(self, matricula: str) -> Medico:
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoError(f"Médico con matrícula {matricula} no encontrado.")
        return self.__medicos[matricula]

    # Turnos
    def agendar_turno(self, turno: Turno):
        if turno in self.__turnos:
            raise TurnoYaExisteError("El turno ya está agendado.")
        self.__turnos.append(turno)

    def obtener_turnos(self):
        return list(self.__turnos)

    # Historias clínicas
    def obtener_historia_clinica(self, dni: str) -> HistoriaClinica:
        if dni not in self.__historias_clinicas:
            raise HistoriaClinicaNoEncontradaError(f"Historia clínica para DNI {dni} no encontrada.")
        return self.__historias_clinicas[dni]
