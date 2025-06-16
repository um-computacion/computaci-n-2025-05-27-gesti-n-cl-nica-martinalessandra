# excepciones.py

class ClinicaError(Exception):
    """Clase base para las excepciones de la clínica."""
    pass

class PacienteYaExisteError(ClinicaError):
    """Se lanza cuando se intenta agregar un paciente con DNI ya existente."""
    pass

class PacienteNoEncontradoError(ClinicaError):
    """Se lanza cuando un paciente no está registrado en la clínica."""
    pass

class MedicoYaExisteError(ClinicaError):
    """Se lanza cuando se intenta agregar un médico con matrícula ya existente."""
    pass

class MedicoNoEncontradoError(ClinicaError):
    """Se lanza cuando un médico no está registrado en la clínica."""
    pass

class TurnoYaExisteError(ClinicaError):
    """Se lanza cuando se intenta agendar un turno que ya existe."""
    pass

class TurnoNoEncontradoError(ClinicaError):
    """Se lanza cuando se busca un turno que no existe."""
    pass

class HistoriaClinicaNoEncontradaError(ClinicaError):
    """Se lanza cuando no se encuentra la historia clínica de un paciente."""
    pass
