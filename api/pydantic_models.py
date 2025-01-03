from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class ModelName(str, Enum):
    GPT4_O = "gpt-4o"
    GPT3_5_turbo = "gpt-3.5-turbo"

class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default = None)
    model: ModelName = Field(default = ModelName.GPT3_5_turbo)

class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: ModelName

class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_timestamp: datetime

class DeleteFileRequest(BaseModel):
    file_id: int