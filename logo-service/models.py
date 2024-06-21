# generated by fastapi-codegen:
#   filename:  api-definition/logoservice.yaml
#   timestamp: 2024-06-20T18:48:54+00:00

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Info(BaseModel):
    generation_date: Optional[datetime] = Field(None, alias='generation-date')
    systemDescription: Optional[str] = None
    apiVersion: Optional[str] = None


class Logo(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    creator: Optional[str] = Field(None, description='logo creator')
    imageUri: Optional[str] = None