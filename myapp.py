from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from jinja2 import Environment, FileSystemLoader
from models import Author, User, UserCurrency
from utils.currencies_api import get_currencies, get_currency_history

env = Environment(loader=FileSystemLoader("templates"))

author = Author("Ekaterina Shukalovich", "P3121")

users = [
    User(1, "Алиса"),
    User(2, "Евгений"),
    User(3, "Андрей")
]

subscriptions = [
    UserCurrency(1, "R01235"),   # USD
    UserCurrency(1, "R01239"),   # EUR
    UserCurrency(2, "R01375"),   # CNY
    UserCurrency(3, "R01090B"),  # BYN
]


class MyHandler(BaseHTTPRequestHandler):

    # функция для показа HTML
    def show(self, filename, **params):
        template = env.get_template(filename)
        html = template.render(**params)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def do_GET(self):
        url = urlparse(self.path)
        path = url.path
        args = parse_qs(url.query)

    

        menu = [
            {"caption": "Главная", "href": "/"},
            {"caption": "Пользователи", "href": "/users"},
            {"caption": "Курсы валют", "href": "/currencies"},
            {"caption": "Автор проекта", "href": "/author_project"}
        ]

        # ---------------- Главная страница ----------------
        if path == "/":
            self.show(
                "index.html",
                navigation=menu,
                myapp="CurrenciesListApp v1.0",
                author_name=author.name,
                group=author.group,
                a_variable="Добро пожаловать в приложение!"
            )
            return

        # ---------------- Список пользователей ----------------
        if path == "/users":
            self.show("users.html", navigation=menu, users=users)
            return
        # ---------------- Сведения об авторе ----------------
        if path == "/author_project":
            self.show("author_project.html", navigation=menu, author_name=author.name, group=author.group)
            return

        # ---------------- Страница пользователя ----------------
        if path == "/user":

    # ID
            if "id" not in args:
                self.show("error.html", message="Не указан id пользователя")
                return

            user_id = int(args["id"][0])

    # Поиск пользователя
            current_user = None
            for u in users:
                if u.id == user_id:
                    current_user = u

            if current_user is None:
                self.show("error.html", message="Пользователь не найден")
                return

    # Текущие курсы
            try:
                all_curr = get_currencies()
            except:
                all_curr = {}

    # Список валют пользователя
            user_currs = []
            for sub in subscriptions:
                if sub.user_id == user_id:
                    cid = sub.currency_id
                    if cid in all_curr:
                        user_currs.append(all_curr[cid])

    # История валют за 3 месяца
            history_by_currency = {}

            for curr in user_currs:
                cid = curr["id"]
                hist = get_currency_history(cid, months=3)
                history_by_currency[cid] = {
                    "char_code": curr["char_code"],
                    "history": hist
                }

    # Рендер страницы
            self.show(
                "user.html",
                navigation=menu,
                user=current_user,
                currencies=user_currs,
                labels=labels,
                datasets=datasets,
                history=history_by_currency
            )
            return



        # ---------------- Курсы валют ----------------
        if path == "/currencies":
            try:
                currs = get_currencies()
                curr_list = list(currs.values())
            except:
                curr_list = []

            self.show("currencies.html", navigation=menu, currencies=curr_list)
            return

        # ---------------- Ошибка ----------------
        self.show("error.html", message="Страница не найдена")



if __name__ == '__main__':
    print("server is running on http://localhost:8080")
    httpd = HTTPServer(('localhost', 8080), MyHandler)
    httpd.serve_forever()
