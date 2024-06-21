from typing import List
from typing import Any
from dataclasses import dataclass


@dataclass
class Variant:
    sku_thumb_images: List[str]
    sku_swatch_images: List[str]
    sku_color_group: str

    @staticmethod
    def from_dict(obj: Any) -> 'Variant':
        # _sku_thumb_images = [.from_dict(y) for y in obj.get("sku_thumb_images")]
        _sku_thumb_images = [obj.get("sku_thumb_images")]
        # _sku_swatch_images = [.from_dict(y) for y in obj.get("sku_swatch_images")]
        _sku_swatch_images = [obj.get("sku_swatch_images")]
        _sku_color_group = str(obj.get("sku_color_group"))
        return Variant(_sku_thumb_images, _sku_swatch_images, _sku_color_group)


@dataclass
class Doc:
    sale_price: float
    price: float
    url: str
    title: str
    pid: str
    brand: str
    thumb_image: str
    variants: List[Variant]

    @staticmethod
    def from_dict(obj: Any) -> 'Doc':
        _sale_price = float(obj.get("sale_price"))
        _price = float(obj.get("price"))
        _url = str(obj.get("url"))
        _title = str(obj.get("title"))
        _pid = str(obj.get("pid"))
        _brand = str(obj.get("brand"))
        _thumb_image = str(obj.get("thumb_image"))
        _variants = [Variant.from_dict(y) for y in obj.get("variants")]
        return Doc(_sale_price, _price, _url, _title, _pid, _brand, _thumb_image, _variants)


@dataclass
class Gender:
    name: str
    count: int

    @staticmethod
    def from_dict(obj: Any) -> 'Gender':
        _name = str(obj.get("name"))
        _count = int(obj.get("count"))
        return Gender(_name, _count)


@dataclass
class Response:
    numFound: int
    start: int
    docs: List[Doc]

    @staticmethod
    def from_dict(obj: Any) -> 'Response':
        _numFound = int(obj.get("numFound"))
        _start = int(obj.get("start"))
        _docs = [Doc.from_dict(y) for y in obj.get("docs")]
        return Response(_numFound, _start, _docs)


@dataclass
class ReviewsCount:
    name: str
    count: int

    @staticmethod
    def from_dict(obj: Any) -> 'ReviewsCount':
        _name = str(obj.get("name"))
        _count = int(obj.get("count"))
        return ReviewsCount(_name, _count)


@dataclass
class FacetFields:
    gender: List[Gender]

    @staticmethod
    def from_dict(obj: Any) -> 'FacetFields':
        _gender = [Gender.from_dict(y) for y in obj.get("gender")]
        return FacetFields(_gender)


@dataclass
class Root:
    response: Response
    facet_fields: FacetFields

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _response = Response.from_dict(obj.get("response"))
        _facet_fields = FacetFields.from_dict(obj.get("facet_fields"))
        return Root(_response, _facet_fields)
