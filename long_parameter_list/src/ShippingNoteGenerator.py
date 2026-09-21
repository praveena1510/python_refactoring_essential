from dataclasses import dataclass


class ShippingNoteGenerator:

    def generate_shipping_note(self, order, customer=None, address=None):
        full_name = customer.first_name + " " + customer.last_name

        address = address.line1 + ", " + (
            address.line2 + ", " if address.line2 is not None else ""
        ) + address.city + ", " + address.postcode + ", " + address.country

        return (
            "SHIPPING NOTE\n"
            f"Order: {order.order_id}\n"
            f"Customer: {full_name}\n"
            f"Ship To: {address}\n"
            f"Item: {order.item_description}\n"
            f"Quantity: {order.quantity}"
        )


@dataclass
class Order:
    order_id: str
    item_description: str
    quantity: int


@dataclass
class Customer:
    first_name:str
    last_name:str


@dataclass
class Address:
    line1: str
    line2: str
    city: str
    postcode: str
    country: str


