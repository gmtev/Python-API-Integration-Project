import requests

def get_price(cur_pair):
    url = f"https://www.freeforexapi.com/api/live?pairs={cur_pair}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][f"{cur_pair}"]["rate"]
        return f'Current rate for {cur_pair[:3]} to {cur_pair[3:]} is: {rate}'
    else:
        return 'Error fetching data!'


currency_pairs = {
    "1": 'EURUSD',
    "2": "EURGBP",
    "3": "GBPUSD",
    "4": "USDJPY",
    "5": "AUDUSD",
    "6": "USDCHF",
    "7": "NZDUSD",
    "8": "USDCAD",
    "9": "USDZAR"
}

print('''Welcome to the currency exchange rates API interface!
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
        
    cur_pair = currency_pairs.get(user_input)
    if cur_pair:
        print(get_price(cur_pair))
    else:
        print("Incorrect input, try again!")

