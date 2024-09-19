"""
(*) დაწერეთ პროგრამა რომელიც მიიღებს წელს, თვეს და დღეს,
როცა მომხმარებელმა იყიდა ბიტკოინი,
ასევე მიიღებს დოლარში თანხას, რომელიც შემოყვანილ თარიღში გადაიხადა ბიტკოინის შესაძენად
და ეკრანზე გამოიტანს დოლარში თანხას რომელიც მოიგო ან დაკარგა დღევანდელი ფასის გათვალისწინებით.
იხ module forex-python

input:
date - წელს, თვეს და დღეს
usd_amount - თანხა

Output:
loss or gain

"""
import datetime
from forex_python.bitcoin import BtcConverter

btc_converter = BtcConverter()

print("Current price", btc_converter.get_latest_price('EUR'))
print("Price in 2016", btc_converter.get_previous_price('EUR', datetime.datetime.now()))

# date_time = datetime.datetime(2016, 5, 18, 19, 39, 36, 815417)
# btc_converter.convert_to_btc_on(5000, 'USD', date_time)   # convert_to_btc_on(5000, 'USD', date_obj)