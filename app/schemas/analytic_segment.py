from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


from app.schemas.message import ApiResponse
from typing import List, Dict


class AnalyticSegmentBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int | None = None
    category: str
    site_identifier: str
    start_date: str | None = None
    end_date: str | None = None
    country: str | None = None
    language: str | None = None
    device_type: str | None = None


class AnalyticSegmentFilters(AnalyticSegmentBase):
    skip: int | None = 0
    limit: int | None = 100


class AnalyticSegmentData(AnalyticSegmentBase):
    pass


class AnalyticSegmentResponse(ApiResponse):
    message: str = "Analytic Segment API Response"
    data: AnalyticSegmentData | List[AnalyticSegmentData]
    detail: Dict[str, Any] | None = {"key": "val"}
