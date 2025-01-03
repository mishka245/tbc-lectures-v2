from pprint import pprint

import requests

URL = "https://www.mymarket.ge/ka/search/?Keyword=%E1%83%92%E1%83%94%E1%83%9C%E1%83%94%E1%83%A0%E1%83%90%E1%83%A2%E1%83%9D%E1%83%A0%E1%83%98&Page=1&SortID=1"


def get_latest_products():
    response = requests.post("https://api.mymarket.ge/api/ka/products",
                             json={"Keyword": "გენერატორი", "Page": 1, "SortID": 1, "Limit": 28, "WithShops": True},
                             headers={"Content-Type": "application/json"}
                             )
    print(response.status_code)
    pprint(response.text)
    return None

def main():
    products = get_latest_products()
    print(products)


if __name__ == "__main__":
    main()
