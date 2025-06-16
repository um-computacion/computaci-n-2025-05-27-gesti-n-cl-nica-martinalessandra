class Turno:
    def __init__(self, paciente, medico, fecha_hora):
        if paciente is None:
            raise ValueError("El paciente no puede ser None.")
        if medico is None:
            raise ValueError("El médico no puede ser None.")
        if fecha_hora is None:
            raise ValueError("La fecha y hora no puede ser None.")
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora

    def obtener_paciente(self):
        return self.__paciente

    def obtener_medico(self):
        return self.__medico

    def obtener_fecha_hora(self):
        return self.__fecha_hora

    def __str__(self):
        return f"Turno:\nPaciente: {self.__paciente}\nMédico: {self.__medico}\nFecha y Hora: {self.__fecha_hora}"
