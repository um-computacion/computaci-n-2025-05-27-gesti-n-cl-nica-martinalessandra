import unittest
from especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):

    def test_crear_especialidad_valida(self):
        esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.assertEqual(esp.obtener_especialidad(), "Cardiología")
        self.assertTrue(esp.verificar_dia("lunes"))
        self.assertTrue(esp.verificar_dia("LUNES"))
        self.assertFalse(esp.verificar_dia("viernes"))
        self.assertIn("lunes", str(esp).lower())

    def test_tipo_vacio_raises(self):
        with self.assertRaises(ValueError):
            Especialidad("", ["lunes"])

    def test_dias_invalidos_raises(self):
        with self.assertRaises(ValueError):
            Especialidad("Pediatría", [])
        with self.assertRaises(ValueError):
            Especialidad("Pediatría", ["", "martes"])

    def test_verificar_dia_sensible_minusculas(self):
        esp = Especialidad("Neurología", ["martes", "viernes"])
        self.assertTrue(esp.verificar_dia("Martes"))
        self.assertTrue(esp.verificar_dia("viernes"))
        self.assertFalse(esp.verificar_dia("domingo"))

    def test_str_formato_correcto(self):
        esp = Especialidad("Dermatología", ["jueves"])
        texto = str(esp)
        self.assertIn("dermatología", texto.lower())
        self.assertIn("jueves", texto.lower())

if __name__ == "__main__":
    unittest.main()
