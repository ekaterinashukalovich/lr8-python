import unittest
from http.server import HTTPServer
from threading import Thread
import requests
from myapp import MyHandler


class TestController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("localhost", 8001), MyHandler)
        cls.thread = Thread(target=cls.server.serve_forever)
        cls.thread.daemon = True
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def test_index_route(self):
        r = requests.get("http://localhost:8001/")
        self.assertEqual(r.status_code, 200)
        self.assertIn("Добро пожаловать", r.text)

    def test_users_route(self):
        r = requests.get("http://localhost:8001/users")
        self.assertEqual(r.status_code, 200)
        self.assertIn("Алиса", r.text)

    def test_currencies_route(self):
        r = requests.get("http://localhost:8001/currencies")
        self.assertEqual(r.status_code, 200)

    def test_user_with_id(self):
        r = requests.get("http://localhost:8001/user?id=1")
        self.assertEqual(r.status_code, 200)
        self.assertIn("Алиса", r.text)

    def test_user_without_id(self):
        r = requests.get("http://localhost:8001/user")
        self.assertEqual(r.status_code, 200)
        self.assertIn("Не указан id", r.text)
