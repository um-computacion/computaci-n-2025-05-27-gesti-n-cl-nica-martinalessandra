import unittest
from receta import Receta

class TestReceta(unittest.TestCase):

    def test_crear_receta_valida(self):
        r = Receta(["Paracetamol", "Ibuprofeno"], "Tomar después de las comidas")
        self.assertIn("Paracetamol", r.obtener_medicamentos())
        self.assertIn("Ibuprofeno", r.obtener_medicamentos())
        self.assertEqual(r.obtener_indicaciones(), "Tomar después de las comidas")
        self.assertIn("paracetamol", str(r).lower())

    def test_medicamentos_invalidos_raises(self):
        with self.assertRaises(ValueError):
            Receta([], "Indicación válida")
        with self.assertRaises(ValueError):
            Receta(["", "Ibuprofeno"], "Indicación válida")

    def test_indicaciones_vacias_raises(self):
        with self.assertRaises(ValueError):
            Receta(["Paracetamol"], "")

    def test_obtener_medicamentos_copia(self):
        r = Receta(["Aspirina"], "Tomar en ayunas")
        meds = r.obtener_medicamentos()
        meds.append("Otro medicamento")
        self.assertNotIn("Otro medicamento", r.obtener_medicamentos())

    def test_str_formato(self):
        r = Receta(["Amoxicilina"], "Dosis cada 8 horas")
        texto = str(r)
        self.assertIn("amoxicilina", texto.lower())
        self.assertIn("cada 8 horas", texto.lower())

if __name__ == "__main__":
    unittest.main()
