class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not dni.strip():
            raise ValueError("El DNI no puede estar vacío.")
        if not self._validar_fecha(fecha_nacimiento):
            raise ValueError("La fecha de nacimiento debe tener formato dd/mm/aaaa.")
        self.__nombre = nombre.strip()
        self.__dni = dni.strip()
        self.__fecha_nacimiento = fecha_nacimiento.strip()

    def obtener_dni(self) -> str:
        return self.__dni

    def __str__(self) -> str:
        return f"Paciente: {self.__nombre} (DNI: {self.__dni}, Fecha Nac.: {self.__fecha_nacimiento})"

    @staticmethod
    def _validar_fecha(fecha: str) -> bool:
        import re
        # Validar formato dd/mm/aaaa
        return bool(re.match(r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$", fecha))
