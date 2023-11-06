# %% Module imports
from pydantic import BaseModel, Field
from typing import List, Dict


# %% Schema Classes

class Point(BaseModel):
    x: int = Field(...)
    y: int = Field(...)


class BoundingBoxPoints(BaseModel):
    points: Point


class MatchingCad(BaseModel):
    cad_id: str = Field(...)
    image: bytes = Field(...)
    gt: bool = Field(default=False)


class Block(BaseModel):
    block_id: str = Field(...)
    status: str = Field(...)
    image: bytes = Field(...)
    bounding_boxes: List[BoundingBoxPoints]
    matching_cads: List[MatchingCad]


class PeYard(BaseModel):
    yard_id: str = Field(...)
    location: str = Field(default='DOCK1')
    image: bytes = Field(...)
    blocks: List[Block]
