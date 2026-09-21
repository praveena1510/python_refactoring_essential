from dataclasses import dataclass


class ShippingNoteGenerator:

    def generate_shipping_note(self, address_line1, address_line2, city, postcode, country, order_id, item_description,
                               quantity, customer=None, address=None):
        full_name = customer.first_name + " " + customer.last_name

        address = address_line1 + ", " + (
            address_line2 + ", " if address_line2 is not None else ""
        ) + city + ", " + postcode + ", " + country

        return (
            "SHIPPING NOTE\n"
            f"Order: {order_id}\n"
            f"Customer: {full_name}\n"
            f"Ship To: {address}\n"
            f"Item: {item_description}\n"
            f"Quantity: {quantity}"
        )
@dataclass
class Customer:
    first_name:str
    last_name:str


@dataclass
class Address:
    address_line1: str
    address_line2: str
    city: str
    postcode: str
    country: str



