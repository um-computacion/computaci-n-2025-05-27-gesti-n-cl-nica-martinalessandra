from receta import Receta

class HistoriaClinica:
    def __init__(self):
        self.diagnosticos = []
        self.recetas = []

    def agregar_diagnostico(self, diagnostico: str):
        if not isinstance(diagnostico, str) or not diagnostico.strip():
            raise ValueError("El diagnóstico debe ser una cadena no vacía.")
        self.diagnosticos.append(diagnostico.strip())

    def agregar_receta(self, receta: Receta):
        if not isinstance(receta, Receta):
            raise TypeError("Debe proporcionar un objeto Receta válido.")
        self.recetas.append(receta)

    def listar_diagnosticos(self):
        return self.diagnosticos.copy()

    def listar_recetas(self):
        return self.recetas.copy()

    def obtener_historial(self):
        return {
            "diagnosticos": self.listar_diagnosticos(),
            "recetas": self.listar_recetas()
        }
