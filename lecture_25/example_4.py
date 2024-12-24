
class LoggerMixin:
    def log(self, message):
        print("Logging message: ", message)

class Database:
    def save(self, data):
        self.log(str(data))
        print("Saving data to database: ", data)

class PaymentService:
    def send_payment(self, amount):
        self.log(str(amount))
        print("Sending payment: ", amount)


class LoggerDatabase(Database, LoggerMixin):
    pass

class LoggerPaymentService(PaymentService, LoggerMixin):
    pass
