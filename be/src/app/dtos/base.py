from pydantic import BaseModel, Field


class BaseSearchParams(BaseModel):
    limit: int = Field(
        default=10,
        lt=100,
        title="limit",
        alias='limit'
    )
    offset: int = Field(
        default=0,
        lt=100,
        title="offset",
        alias='offset'
    )
