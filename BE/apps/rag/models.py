from enum import Enum
from pydantic import BaseModel, Field

class OrganizationEnum(str, Enum):
    apple = 'apple'
    nvidia = 'nvidia'
    toyota = 'toyota'

class ModelEnum(str, Enum):
    gpt35 = 'gpt-3.5-turbo-instruct'
    babbage002 = 'babbage-002'
    davinci002 = 'davinci-002'


class QueryModel(BaseModel):
    organization: OrganizationEnum
    prompt: str
    model: ModelEnum
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "organization": "apple",
                "prompt": "My new prompt",
            }
        }
