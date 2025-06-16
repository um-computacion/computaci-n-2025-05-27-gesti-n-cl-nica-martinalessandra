import unittest
import sys
import os

# Ajustar el path para importar desde la carpeta src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from historia_clinica import HistoriaClinica
from receta import Receta

class TestHistoriaClinica(unittest.TestCase):

    def setUp(self):
        self.historia = HistoriaClinica()

    def test_agregar_diagnostico(self):
        self.historia.agregar_diagnostico("Gripe")
        self.assertIn("Gripe", self.historia.diagnosticos)

    def test_agregar_receta_valida(self):
        receta = Receta("Paracetamol", "500mg cada 8 horas")
        self.historia.agregar_receta(receta)
        self.assertEqual(len(self.historia.recetas), 1)
        self.assertEqual(self.historia.recetas[0].medicamento, "Paracetamol")

    def test_listar_diagnosticos(self):
        self.historia.agregar_diagnostico("Dolor de cabeza")
        self.historia.agregar_diagnostico("Migraña")
        diagnosticos = self.historia.listar_diagnosticos()
        self.assertEqual(diagnosticos, ["Dolor de cabeza", "Migraña"])

    def test_listar_recetas(self):
        receta1 = Receta("Ibuprofeno", "400mg cada 6 horas")
        receta2 = Receta("Amoxicilina", "500mg cada 12 horas")
        self.historia.agregar_receta(receta1)
        self.historia.agregar_receta(receta2)
        recetas = self.historia.listar_recetas()
        self.assertEqual(len(recetas), 2)
        self.assertEqual(recetas[1].medicamento, "Amoxicilina")

    def test_historial_clinico_completo(self):
        self.historia.agregar_diagnostico("Sinusitis")
        receta = Receta("Loratadina", "10mg diaria")
        self.historia.agregar_receta(receta)
        historial = self.historia.obtener_historial()
        self.assertIn("Sinusitis", historial["diagnosticos"])
        self.assertEqual(historial["recetas"][0].medicamento, "Loratadina")

if __name__ == "__main__":
    unittest.main()
