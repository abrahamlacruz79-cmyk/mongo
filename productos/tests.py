from unittest.mock import patch

from bson import ObjectId
from django.test import TestCase


class ListarProductosTests(TestCase):
    @patch("productos.views.coleccion_productos.find")
    def test_lista_usa_el_id_de_mongodb_en_los_enlaces(self, mock_find):
        identificador = ObjectId("507f1f77bcf86cd799439011")
        mock_find.return_value.sort.return_value = [
            {
                "_id": identificador,
                "nombre": "Producto de prueba",
                "precio": 10.5,
                "cantidad": 3,
            }
        ]

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'href="/editar/{identificador}/"')
        self.assertContains(
            response,
            f'action="/eliminar/{identificador}/"',
        )
