from pydantic import BaseModel, Field, ConfigDict


class ProductPostRequestSchema(BaseModel):
    articule: int = Field(
        ..., description="Артикул товара на wildberries", examples=[211695539]
    )


class ProductExternalSchena(ProductPostRequestSchema):
    name: str = Field(
        ..., description="Название продукта", 
        examples=["Гель для бровей версия 2.0 супер сильная фиксация"]
    )
    cost: int = Field(
        ..., description="Цена", examples=[133200]
    )
    rating: float = Field(
        ..., description="Рейтинг товара", examples=[5.0]
    )
    total_quantity: int = Field(
        ..., description="Общее количество на всех складах", examples=[90570]
    )


class ProductSchema(ProductExternalSchena):
    product_id: int = Field(
        ..., description="ID продукта", examples=[2]
    )

    model_config = ConfigDict(from_attributes=True)