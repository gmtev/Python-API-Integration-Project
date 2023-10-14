import requests


def get_price_eur_usd():
    url = "https://www.freeforexapi.com/api/live?pairs=EURUSD"
    response = requests.get(url)
    if response.status_code == 200:
        date = response.json()
        rate = date["rates"]["EURUSD"]["rate"]
        return f'Current rate for EUR to USD is: {rate}'
    else:
        return 'Error fetching data!'


def get_price_eur_gbp():
    url = "https://www.freeforexapi.com/api/live?pairs=EURGBP"
    response = requests.get(url)
    if response.status_code == 200:
        date = response.json()
        rate = date["rates"]["EURGBP"]["rate"]
        return f'Current rate for EUR to GBP is: {rate}'
    else:
        return 'Error fetching data!'


def get_price_gbp_usd():
    url = "https://www.freeforexapi.com/api/live?pairs=GBPUSD"
    response = requests.get(url)
    if response.status_code == 200:
        date = response.json()
        rate = date["rates"]["GBPUSD"]["rate"]
        return f'Current rate for GBP to USD is: {rate}'
    else:
        return 'Error fetching data!'


def get_price_usd_jpy():
    url = "https://www.freeforexapi.com/api/live?pairs=USDJPY"
    response = requests.get(url)
    if response.status_code == 200:
        date = response.json()
        rate = date["rates"]["USDJPY"]["rate"]
        return f'Current rate for USD to JPY is: {rate}'
    else:
        return 'Error fetching data!'


def get_price_aud_usd():
    url = "https://www.freeforexapi.com/api/live?pairs=AUDUSD"
    response = requests.get(url)
    if response.status_code == 200:
        date = response.json()
        rate = date["rates"]["AUDUSD"]["rate"]
        return f'Current rate for AUD to USD is: {rate}'
    else:
        return 'Error fetching data!'


def get_price_usd_chf():
    url = "https://www.freeforexapi.com/api/live?pairs=USDCHF"
    response = requests.get(url)
    if response.status_code == 200:
        date = response.json()
        rate = date["rates"]["USDCHF"]["rate"]
        return f'Current rate for USD to CHF is: {rate}'
    else:
        return 'Error fetching data!'


def get_price_nzd_usd():
    url = "https://www.freeforexapi.com/api/live?pairs=NZDUSD"
    response = requests.get(url)
    if response.status_code == 200:
        date = response.json()
        rate = date["rates"]["NZDUSD"]["rate"]
        return f'Current rate for NZD to USD is: {rate}'
    else:
        return 'Error fetching data!'


def get_price_usd_cad():
    url = "https://www.freeforexapi.com/api/live?pairs=USDCAD"
    response = requests.get(url)
    if response.status_code == 200:
        date = response.json()
        rate = date["rates"]["USDCAD"]["rate"]
        return f'Current rate for USD to CAD is: {rate}'
    else:
        return 'Error fetching data!'


def get_price_usd_zar():
    url = "https://www.freeforexapi.com/api/live?pairs=USDZAR"
    response = requests.get(url)
    if response.status_code == 200:
        date = response.json()
        rate = date["rates"]["USDZAR"]["rate"]
        return f'Current rate for USD to ZAR is: {rate}'
    else:
        return "Error fetching data!"


current_rate_eur_usd = get_price_eur_usd()
current_rate_eur_gbp = get_price_eur_gbp()
current_rate_gbp_usd = get_price_gbp_usd()
current_rate_usd_jpy = get_price_usd_jpy()
current_rate_aud_usd = get_price_aud_usd()
current_rate_usd_chf = get_price_usd_chf()
current_rate_nzd_usd = get_price_nzd_usd()
current_rate_usd_cad = get_price_usd_cad()
current_rate_usd_zar = get_price_usd_zar()

print(f'''Welcome to the currency exchange rates API interface!
The available options are:
        "EURUSD" - 1
        "EURGBP" - 2
        "GBPUSD" - 3
        "USDJPY" - 4
        "AUDUSD" - 5
        "USDCHF" - 6
        "NZDUSD" - 7
        "USDCAD" - 8
        "USDZAR" - 9 
        "Exit" - 0
''')
while True:
    user_input = input("Please, input the chosen number:")
    if user_input == "0":
        print("Have a nice day!")
        break
    elif user_input == "1":
        print(get_price_eur_usd())
    elif user_input == "2":
        print(get_price_eur_gbp())
    elif user_input == "3":
        print(get_price_gbp_usd())
    elif user_input == "4":
        print(get_price_usd_jpy())
    elif user_input == "5":
        print(get_price_aud_usd())
    elif user_input == "6":
        print(get_price_usd_chf())
    elif user_input == "7":
        print(get_price_nzd_usd())
    elif user_input == "8":
        print(get_price_usd_cad())
    elif user_input == "9":
        print(get_price_usd_zar())
