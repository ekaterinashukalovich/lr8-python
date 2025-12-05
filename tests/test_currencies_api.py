import unittest
from unittest.mock import patch
from utils.currencies_api import get_currencies
import requests


class TestCurrenciesAPI(unittest.TestCase):

    @patch("requests.get")
    def test_get_currencies_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = """
        <ValCurs>
            <Valute ID="R01235">
                <NumCode>840</NumCode>
                <CharCode>USD</CharCode>
                <Nominal>1</Nominal>
                <Name>Доллар США</Name>
                <Value>92,45</Value>
            </Valute>
        </ValCurs>
        """.encode("utf-8")

        data = get_currencies()
        self.assertIn("R01235", data)
        self.assertEqual(data["R01235"]["char_code"], "USD")

    @patch("requests.get")
    def test_network_error(self, mock_get):
        mock_get.return_value.status_code = 500
        with self.assertRaises(ConnectionError):
            get_currencies()

    @patch("requests.get")
    def test_invalid_xml(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b"<invalid></xml>"
        with self.assertRaises(ValueError):
            get_currencies()

    @patch("requests.get")
    def test_no_currencies(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b"<ValCurs></ValCurs>"
        with self.assertRaises(ValueError):
            get_currencies()
