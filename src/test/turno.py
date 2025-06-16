import unittest
from turno import Turno
from paciente import Paciente
from medico import Medico
from datetime import datetime

class TestTurno(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan", "Pérez", "12345678", "1234567890", "Calle Falsa 123")
        self.medico = Medico("Ana", "Gómez", "98765432", "Ginecología")
        self.fecha_hora = datetime(2025, 6, 15, 14, 30)

    def test_crear_turno_valido(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora)
        self.assertEqual(turno.obtener_paciente(), self.paciente)
        self.assertEqual(turno.obtener_medico(), self.medico)
        self.assertEqual(turno.obtener_fecha_hora(), self.fecha_hora)
        self.assertIn("Juan", str(turno))
        self.assertIn("Ana", str(turno))
        self.assertIn("2025", str(turno))

    def test_turno_paciente_none_raises(self):
        with self.assertRaises(ValueError):
            Turno(None, self.medico, self.fecha_hora)

    def test_turno_medico_none_raises(self):
        with self.assertRaises(ValueError):
            Turno(self.paciente, None, self.fecha_hora)

    def test_turno_fecha_hora_none_raises(self):
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, None)

    def test_str_formato(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora)
        texto = str(turno)
        self.assertIn("turno", texto.lower())
        self.assertIn("juan", texto.lower())
        self.assertIn("ana", texto.lower())

if __name__ == "__main__":
    unittest.main()
