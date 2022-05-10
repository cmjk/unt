from dataclasses import dataclass

from bs4 import BeautifulSoup


@dataclass
class ProductItem:
    """
    Represents a product
    """
    name: str
    price: float

    @staticmethod
    def from_html(html: str) -> list["ProductItem"]:
        """
        Constructs a list of ProductItems from API output by parsing HTML
        """
        parsed = BeautifulSoup(html, "html.parser")
        return [
            ProductItem(
                name=item.select_one(".product-title").text,
                price=float(item.select_one(".actual-price").text.lstrip("$").replace(",", "")))
            for item in parsed.select(".item-box")]


@dataclass
class Products:
    """
    Stores products
    """
    asus_n551: ProductItem = ProductItem(name="Asus N551JK-XO076H Laptop",
                                         price=1500.0)
    samsung_series9: ProductItem = ProductItem(name="Samsung Series 9 NP900X4C Premium Ultrabook",
                                               price=1590.0)
    hp_spectre: ProductItem = ProductItem(name="HP Spectre XT Pro UltraBook",
                                          price=1350.0)
    hp_envy: ProductItem = ProductItem(name="HP Envy 6-1180ca 15.6-Inch Sleekbook",
                                       price=1460.0)
    lenovo_thinkpad: ProductItem = ProductItem(name="Lenovo Thinkpad X1 Carbon Laptop",
                                               price=1360.0)
