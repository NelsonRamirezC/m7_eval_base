from laboratorio.models import DirectorGeneral

from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DirectorGeneralTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.director = DirectorGeneral(nombre = "Miguel García")
        cls.director.save()

    def test_model_content(self):
        """Nombre de la instancia / objeto corresponde al de la creación"""
        logger.info("Iniciando prueba: Nombre de la instancia / objeto corresponde al de la creación")
        self.assertEqual(self.director.nombre, "Miguel García")
        
    def test_verificacion_existencia(self):
        """Validar creación el DB de modelo DirectorGeneral"""
        logger.info("Iniciando prueba: creación el DB de modelo DirectorGeneral")
    
        director = DirectorGeneral.objects.get(id=self.director.id)
        self.assertEqual(director.nombre, self.director.nombre)
        
    def test_cambiar_nombre_director(self):
        """Validar cambio de nombre del director"""
        logger.info("Iniciando prueba: cambio de nombre del director")
         
        director = DirectorGeneral.objects.get(id=self.director.id)
        nuevo_nuevo = "Pedro García"
        director.nombre = nuevo_nuevo
        director.save()
        
        self.assertEqual(director.nombre, nuevo_nuevo, "Nombre no coincide con lo esperado.")
    
    def test_nombre_mayusculas(self):
        """Validar retorno función nombre_mayusculas"""
        logger.info("Iniciando prueba: retorno función nombre_mayusculas")
        nombre_mayusculas = self.director.nombre_mayusculas()
        nombre = self.director.nombre.upper()
        
        self.assertEqual(nombre_mayusculas, nombre)
        
        

