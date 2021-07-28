import requests  # импортируем библиотеку

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.split("</Valute>")  # получаем данные,
# конвертируем, формируем список из подстрок (по разделителю "</Valute>")
currency = "R01820"  # код искомой валюты

for i in response:  # проход по всем подстрокам в списке
    if i.count(currency):  # если в i-той подстроке есть искомая валюта
        nominal = (i[i.find('<Nominal>') + len('<Nominal>'):i.find('</Nominal>')])  # находим номинал, т.к. для
        # разных валют он разный (делаем срез так, чтобы взять значение между '<Nominal>' и '</Nominal>')
        name = (i[i.find('<Name>') + len('<Name>'):i.find('</Name>')])  # аналогично ищем название валюты
        value = (i[i.find('<Value>') + len('<Value>'):i.find('</Value>')])  # аналогично ищем стоимость
        print(f"{nominal} {name} стоит {value} рублей")  # выводим результат
