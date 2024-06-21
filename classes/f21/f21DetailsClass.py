from typing import List
from typing import Any
from dataclasses import dataclass


@dataclass
class Inventory:
    id: str
    ats: float
    stock_level: float

    @staticmethod
    def from_dict(obj: Any) -> 'Inventory':
        _id = str(obj.get("id"))
        _ats = float(obj.get("ats"))
        _stock_level = float(obj.get("stock_level"))
        return Inventory(_id, _ats, _stock_level)


@dataclass
class Size:
    Price: float
    SizeId: str
    SizeName: str
    DisplayName: str
    Description: str
    inventories: List[Inventory]
    Available: str

    @staticmethod
    def from_dict(obj: Any) -> 'Size':
        _Price = float(obj.get("Price"))
        _SizeId = str(obj.get("SizeId"))
        _SizeName = str(obj.get("SizeName"))
        _DisplayName = str(obj.get("DisplayName"))
        _Description = str(obj.get("Description"))
        _inventories = [Inventory.from_dict(y) for y in obj.get("inventories")]
        _Available = str(obj.get("Available"))
        return Size(_Price, _SizeId, _SizeName, _DisplayName, _Description, _inventories, _Available)


@dataclass
class Variant:
    ColorId: str
    ColorName: str
    Sizes: List[Size]
    ProductImages: List[str]
    SwatchImage: str

    @staticmethod
    def from_dict(obj: Any) -> 'Variant':
        _ColorId = str(obj.get("ColorId"))
        _ColorName = str(obj.get("ColorName"))
        # _Sizes = [Size.from_dict(y) for y in obj.get("Sizes")]
        _Sizes = [obj.get("Sizes")]
        # _ProductImages = [.from_dict(y) for y in obj.get("ProductImages")]
        _ProductImages = [obj.get("ProductImages")]
        obj.get("sku_swatch_images")
        _SwatchImage = str(obj.get("SwatchImage"))
        return Variant(_ColorId, _ColorName, _Sizes, _ProductImages, _SwatchImage)


@dataclass
class Promotion:
    PromotionId: str
    PromotionType: str
    PromotionLink: str
    PromotionPrice: float
    Message: str

    @staticmethod
    def from_dict(obj: Any) -> 'Promotion':
        _PromotionId = str(obj.get("PromotionId"))
        _PromotionType = str(obj.get("PromotionType"))
        _PromotionLink = str(obj.get("PromotionLink"))
        _PromotionPrice = float(obj.get("PromotionPrice"))
        _Message = str(obj.get("Message"))
        return Promotion(_PromotionId, _PromotionType, _PromotionLink, _PromotionPrice, _Message)


@dataclass
class Product:
    BackorderedQuantity: int
    Brand: str
    CatalogRowNum: int
    CategoryName: str
    ClassType: str
    Description: str
    DisplayName: str
    IntroductionDate: str
    ItemAttr: str
    ItemAttr10: int
    ItemAttr11: str
    ItemAttr12: str
    ItemAttr13: str
    ItemAttr14: str
    ItemAttr15: str
    ItemAttr16: str
    ItemAttr17: str
    ItemAttr18: str
    ItemAttr2: str
    ItemAttr20: str
    ItemAttr3: str
    ItemAttr4: str
    ItemAttr5: str
    ItemAttr6: str
    ItemAttr7: str
    ItemAttr8: str
    ItemAttr9: int
    ItemCode: str
    ListPrice: float
    OId: int
    OnHandQuantity: int
    OriginalPrice: float
    ParentOId: int
    PreorderedQuantity: int
    PrimaryParentCategory: str
    ProductId: str
    ProductShareLinkUrl: str
    RepColorCode: str
    VariantId: str
    Variants: List[Variant]
    Weight: float
    DefaultProductImage: str
    Promotions: List[Promotion]

    @staticmethod
    def from_dict(obj: Any) -> 'Product':
        _BackorderedQuantity = int(obj.get("BackorderedQuantity"))
        _Brand = str(obj.get("Brand"))
        _CatalogRowNum = int(obj.get("CatalogRowNum"))
        _CategoryName = str(obj.get("CategoryName"))
        _ClassType = str(obj.get("ClassType"))
        _Description = str(obj.get("Description"))
        _DisplayName = str(obj.get("DisplayName"))
        _IntroductionDate = str(obj.get("IntroductionDate"))
        _ItemAttr = str(obj.get("ItemAttr"))
        _ItemAttr10 = int(obj.get("ItemAttr10"))
        _ItemAttr11 = str(obj.get("ItemAttr11"))
        _ItemAttr12 = str(obj.get("ItemAttr12"))
        _ItemAttr13 = str(obj.get("ItemAttr13"))
        _ItemAttr14 = str(obj.get("ItemAttr14"))
        _ItemAttr15 = str(obj.get("ItemAttr15"))
        _ItemAttr16 = str(obj.get("ItemAttr16"))
        _ItemAttr17 = str(obj.get("ItemAttr17"))
        _ItemAttr18 = str(obj.get("ItemAttr18"))
        _ItemAttr2 = str(obj.get("ItemAttr2"))
        _ItemAttr20 = str(obj.get("ItemAttr20"))
        _ItemAttr3 = str(obj.get("ItemAttr3"))
        _ItemAttr4 = str(obj.get("ItemAttr4"))
        _ItemAttr5 = str(obj.get("ItemAttr5"))
        _ItemAttr6 = str(obj.get("ItemAttr6"))
        _ItemAttr7 = str(obj.get("ItemAttr7"))
        _ItemAttr8 = str(obj.get("ItemAttr8"))
        _ItemAttr9 = int(obj.get("ItemAttr9"))
        _ItemCode = str(obj.get("ItemCode"))
        _ListPrice = float(obj.get("ListPrice"))
        _OId = int(obj.get("OId"))
        _OnHandQuantity = int(obj.get("OnHandQuantity"))
        _OriginalPrice = float(obj.get("OriginalPrice"))
        _ParentOId = int(obj.get("ParentOId"))
        _PreorderedQuantity = int(obj.get("PreorderedQuantity"))
        _PrimaryParentCategory = str(obj.get("PrimaryParentCategory"))
        _ProductId = str(obj.get("ProductId"))
        _ProductShareLinkUrl = str(obj.get("ProductShareLinkUrl"))
        _RepColorCode = str(obj.get("RepColorCode"))
        _VariantId = str(obj.get("VariantId"))
        _Variants = [Variant.from_dict(y) for y in obj.get("Variants")]
        _Weight = float(obj.get("Weight"))
        _DefaultProductImage = str(obj.get("DefaultProductImage"))
        _Promotions = [Promotion.from_dict(y) for y in obj.get("Promotions")]
        return Product(_BackorderedQuantity, _Brand, _CatalogRowNum, _CategoryName, _ClassType, _Description,
                       _DisplayName, _IntroductionDate, _ItemAttr, _ItemAttr10, _ItemAttr11, _ItemAttr12, _ItemAttr13,
                       _ItemAttr14, _ItemAttr15, _ItemAttr16, _ItemAttr17, _ItemAttr18, _ItemAttr2, _ItemAttr20,
                       _ItemAttr3, _ItemAttr4, _ItemAttr5, _ItemAttr6, _ItemAttr7, _ItemAttr8, _ItemAttr9, _ItemCode,
                       _ListPrice, _OId, _OnHandQuantity, _OriginalPrice, _ParentOId, _PreorderedQuantity,
                       _PrimaryParentCategory, _ProductId, _ProductShareLinkUrl, _RepColorCode, _VariantId, _Variants,
                       _Weight, _DefaultProductImage, _Promotions)


@dataclass
class RootDetails:
    product: Product
    code: str
    errorMessage: str
    authorization: str

    @staticmethod
    def from_dict(obj: Any) -> 'RootDetails':
        _product = Product.from_dict(obj.get("product"))
        _code = str(obj.get("code"))
        _errorMessage = str(obj.get("errorMessage"))
        _authorization = str(obj.get("authorization"))
        return RootDetails(_product, _code, _errorMessage, _authorization)

