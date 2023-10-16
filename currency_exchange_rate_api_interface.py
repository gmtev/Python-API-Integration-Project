import requests


def get_price(cur_pair):
    url = f"https://www.freeforexapi.com/api/live?pairs={cur_pair}"
    response = requests.get(url)
    if response.status_code == 200:
        date = response.json()
        rate = date["rates"][f"{cur_pair}"]["rate"]
        return f'Current rate for {cur_pair[:3]} to {cur_pair[3:]} is: {rate}'
    else:
        return 'Error fetching data!'


eur_usd = 'EURUSD'
eur_gbp = "EURGBP"
gbp_usd = "GBPUSD"
usd_jpy = "USDJPY"
aud_usd = "AUDUSD"
usd_chf = "USDCHF"
nzd_usd = "NZDUSD"
usd_cad = "USDCAD"
usd_zar = "USDZAR"
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
        print(get_price(eur_usd))
    elif user_input == "2":
        print(get_price(eur_gbp))
    elif user_input == "3":
        print(get_price(gbp_usd))
    elif user_input == "4":
        print(get_price(usd_jpy))
    elif user_input == "5":
        print(get_price(aud_usd))
    elif user_input == "6":
        print(get_price(usd_chf))
    elif user_input == "7":
        print(get_price(nzd_usd))
    elif user_input == "8":
        print(get_price(usd_cad))
    elif user_input == "9":
        print(get_price(usd_zar))
    else:
        print("Incorrect input, try again!")

