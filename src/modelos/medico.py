class Medico:
    def __init__(self, nombre: str, matricula: str, especialidad: str):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not matricula.strip():
            raise ValueError("La matrícula no puede estar vacía.")
        if not especialidad.strip():
            raise ValueError("La especialidad no puede estar vacía.")
        self.__nombre = nombre.strip()
        self.__matricula = matricula.strip()
        self.__especialidad = especialidad.strip()

    def obtener_matricula(self) -> str:
        return self.__matricula

    def __str__(self) -> str:
        return f"Médico: {self.__nombre} (Matrícula: {self.__matricula}, Especialidad: {self.__especialidad})"
