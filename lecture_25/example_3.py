
class LoggerMixin:
    def log(self, message):
        print("Logging message: ", message)

class Database(LoggerMixin):

    def save(self, data):
        self.log(str(data))
        print("Saving data to database: ", data)

class PaymentService(LoggerMixin):
    def send_payment(self, amount):
        self.log(str(amount))
        print("Sending payment: ", amount)
