import requests
import sys

red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

print(red + """
IP-CHECKER

                     made by: bars301109
""" + red)


ip = input(cyan + bold + "Введите IP-адрес: " + clear)


api = 'http://ip-api.com/json/'

try:
    response = requests.get(api + ip)
    data = response.json()
    if data['status'] == 'fail':
        print(red + "[~] Невозможно получить данные для указанного IP-адреса." + clear)
        sys.exit(1)

    # Вывод инфы об IP-адресе
    a = lgreen + bold + "[$]"
    b = cyan + bold + "[$]"
    print(a, "[Цель]:", data['query'])
    print(red + "<--------------->" + red)
    print(b, "[Поставщик услуг]:", data['isp'])
    print(red + "<--------------->" + red)
    print(a, "[Оператор]:", data['org'])
    print(red + "<--------------->" + red)
    print(b, "[Город]:", data['city'])
    print(red + "<--------------->" + red)
    print(a, "[Регион]:", data['region'])
    print(red + "<--------------->" + red)
    print(b, "[Долгота]:", data['lon'])
    print(red + "<--------------->" + red)
    print(a, "[Широта]:", data['lat'])
    print(red + "<--------------->" + red)
    print(b, "[Часовой пояс]:", data['timezone'])
    print(red + "<--------------->" + red)
    print(a, "[Почтовый индекс]:", data['zip'])
    print(" " + yellow)

except KeyboardInterrupt:
    print('Прерывание, до свидания!' + lgreen)
    sys.exit(0)

except requests.exceptions.ConnectionError:
    print(red + "[~] Проверьте ваше интернет-соединение!" + clear)
    sys.exit(1)

except Exception as e:
    print(red + f"[~] Произошла ошибка: {str(e)}" + clear)
    sys.exit(1)