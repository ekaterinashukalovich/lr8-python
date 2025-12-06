import xml.etree.ElementTree as ET
import requests
from models.currency import Currency
import datetime

def get_currencies():
    """Получение актуальных курсов валют с сайта ЦБ РФ."""
    url = "https://www.cbr.ru/scripts/XML_daily.asp"

    response = requests.get(url)
    if response.status_code != 200:
        raise ConnectionError("Cannot find currency data")

    try:
        root = ET.fromstring(response.content)
    except Exception:
        raise ValueError("Invalid XML response")

    currencies = {}

    for valute in root.findall("Valute"):
        try:
            curr = Currency(
                currency_id=valute.attrib["ID"],
                num_code=valute.find("NumCode").text,
                char_code=valute.find("CharCode").text,
                name=valute.find("Name").text,
                value=float(valute.find("Value").text.replace(",", ".")),
                nominal=int(valute.find("Nominal").text),
            )

            currencies[valute.attrib["ID"]] = {
                "id": curr.currency_id,
                "num_code": curr.num_code,
                "char_code": curr.char_code,
                "name": curr.name,
                "value": curr.value,
                "nominal": curr.nominal,
            }

        except Exception as e:
            print("Currency parse error:", e)

    if not currencies:
        raise ValueError("No currencies found")

    return currencies

def get_currency_history(currency_id, months=3):
    """Возвращает историю курса валюты за последние N месяцев"""

    # Дата окончания — сегодня
    end = datetime.date.today()

    # Дата начала — 3 месяца назад
    start = end - datetime.timedelta(days=30 * months)

    url = (
        "https://www.cbr.ru/scripts/XML_dynamic.asp?"
        f"date_req1={start.strftime('%d/%m/%Y')}&"
        f"date_req2={end.strftime('%d/%m/%Y')}&"
        f"VAL_NM_RQ={currency_id}"
    )

    response = requests.get(url)
    if response.status_code != 200:
        raise ConnectionError("Cannot fetch historical data")

    try:
        root = ET.fromstring(response.content)
    except:
        raise ValueError("Invalid XML for history")

    history = []

    for record in root.findall("Record"):
        date_str = record.attrib["Date"]
        value_str = record.find("Value").text
        nominal = int(record.find("Nominal").text)

        # Приводим дату к читабельному формату
        d = datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
        v = float(value_str.replace(",", "."))

        history.append({
            "date": d.isoformat(),
            "value": v,
            "nominal": nominal
        })

    return history
