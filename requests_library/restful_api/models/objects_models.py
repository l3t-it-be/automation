from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class DataModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    year: int
    price: int | float
    cpu_model: str = Field(alias='CPU model')
    hard_disk_size: str = Field(alias='Hard disk size')
    color: str | None = Field(default=None)


class RequestObjectModel(BaseModel):
    name: str
    data: DataModel


class ResponseObjectModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str
    created_at: datetime | None = Field(alias='createdAt', default=None)
    data: DataModel


class DeleteResponseModel(BaseModel):
    message: str


class ErrorResponseModel(BaseModel):
    error: str
