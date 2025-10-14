from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    stock: int
    sales_per_day: float
    restock_threshold: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True