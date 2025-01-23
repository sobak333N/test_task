from typing import Optional

from aiohttp import ClientSession
from pydantic import ValidationError

from config import Config
from abstracts import AbsDataFetcher
from schemas import ProductExternalSchena


class HttpFetcher(AbsDataFetcher):
    def __init__(self):
        self.url = Config.FETCH_URL

    async def fetch_data(
        self, session: ClientSession, articule: int
    ) -> Optional[ProductExternalSchena]:
        get_url = self.url + str(articule)
        async with session.get(get_url) as response:
            print(response.text)
            print(response.status)
            if response.status == 200:
                data = await response.json()
                product_data = data.get('data', {}).get('products', [])
                if len(product_data) != 1:
                    print(len(product_data))
                    raise Exception
                product_dict = product_data[0]
                try:
                    product = ProductExternalSchena(
                        articule=product_dict.get('id', None),
                        name=product_dict.get('name', None),
                        cost=product_dict.get('priceU', None),
                        rating=product_dict.get('rating', None),
                        total_quantity=product_dict.get('totalQuantity', None),
                    )
                except ValidationError as e:
                    print(e)
                    raise e
                    print("validation")
                return product
            elif response.status == 404:
                ...
                print("not found")
            raise Exception