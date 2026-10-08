import json

from decimal import Decimal

div = "----"
def calculate_profit(data_file_name: str) -> None:

    with open(data_file_name, "r") as file:
        current_data = json.load(file)
        for trade in current_data:
            print(type(trade))
            print(trade.get("bought"))
            print(type(trade.get("bought")))
            if not trade.get("bought"):
                print("didn't buy")
            print(div)


calculate_profit("app/trades.json")
