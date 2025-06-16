class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        if not tipo.strip():
            raise ValueError("El tipo de especialidad no puede estar vacío.")
        if not dias or not all(isinstance(dia, str) and dia.strip() for dia in dias):
            raise ValueError("Debe proporcionar una lista válida de días de atención.")
        self.__tipo = tipo.strip()
        # Guardamos los días en minúsculas para normalizar
        self.__dias = [dia.strip().lower() for dia in dias]

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        return dia.strip().lower() in self.__dias

    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"
