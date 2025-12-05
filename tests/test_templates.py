import unittest
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


class TestTemplates(unittest.TestCase):

    def setUp(self):
        self.env = Environment(loader=FileSystemLoader("templates"))

    def test_render_user_template(self):
        tmpl = self.env.get_template("user.html")
        html = tmpl.render(
            navigation=[{"caption": "Главная", "href": "/"}],
            user={"name": "Алиса"},
            currencies=[{"name": "Доллар США", "char_code": "USD", "value": 92.5}],
            labels=["Текущее значение"],
            datasets=[[92.5]],
            history={}
        )
        self.assertIn("Алиса", html)
        self.assertIn("Доллар США", html)

    def test_render_loop(self):
        tmpl = self.env.get_template("users.html")
        html = tmpl.render(users=[{"name": "Алиса"}, {"name": "Евгений"}])
        self.assertIn("Алиса", html)
        self.assertIn("Евгений", html)
