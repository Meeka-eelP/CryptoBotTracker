import requests

def get_sat():
        coin = ["BTC"]
        btc_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coin))).json()["RAW"]
        sat = {}
        for i in btc_data:
                sat[i] = {
                "coin": i,
                "price": btc_data[i]["USD"]["PRICE"],
                "change_day": btc_data[i]["USD"]["CHANGEPCT24HOUR"],
                "change_hour": btc_data[i]["USD"]["CHANGEPCTHOUR"]
                }
        return sat

def get_prices():
    coins = ["BTC", "ETH", "BAN", "LTC", "VET", "DOT", "KSM"]

    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
            "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"]
        }

    return data


if __name__ == "__main__":
    print(get_prices())