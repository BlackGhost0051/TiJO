# Naruszona zasada SRP

class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer


class OrderProcessor:
    def __init__(self, order):
        self.order = order

    def process_order(self):
        OrderService._validate_order(self.order)
        DataBaseService._save_order_to_database(self.order)
        MailService._send_confirmation_email(self.order)


class OrderService:
    def _validate_order(self):
        print("Walidacja zamowienia.")


class DataBaseService:
    def _save_order_to_database(self):
        print("Zapisywanie zamowienia do bazy danych.")

class MailService:
    def _send_confirmation_email(self):
        print("Wysylanie e-maila potwierdzajacego.")


order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
processor = OrderProcessor(order)
processor.process_order()

