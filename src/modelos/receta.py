class Receta:
    def __init__(self, medicamentos: list[str], indicaciones: str):
        if not medicamentos or not all(isinstance(med, str) and med.strip() for med in medicamentos):
            raise ValueError("Debe proporcionar una lista válida de medicamentos.")
        if not indicaciones.strip():
            raise ValueError("Las indicaciones no pueden estar vacías.")
        self.__medicamentos = [med.strip() for med in medicamentos]
        self.__indicaciones = indicaciones.strip()

    def obtener_medicamentos(self) -> list[str]:
        return self.__medicamentos.copy()

    def obtener_indicaciones(self) -> str:
        return self.__indicaciones

    def __str__(self) -> str:
        meds = ", ".join(self.__medicamentos)
        return f"Medicamentos: {meds}\nIndicaciones: {self.__indicaciones}"
