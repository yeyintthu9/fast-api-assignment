from sqlalchemy import Column, Integer, String, text

from app.core import security
from app.models.common import DateTimeModelMixin
from app.models.rwmodel import RWModel


class AnalyticSegment(RWModel, DateTimeModelMixin):
    __tablename__ = "analyticsegments"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('analytic_seg_id_seq'::regclass)"),
    )
    category = Column(String(256), nullable=False)
    site_identifier = Column(String(256), nullable=False)
    start_date = Column(String(256), nullable=True)
    end_date = Column(String(256), nullable=True)
    country = Column(String(256), nullable=True)
    language = Column(String(256), nullable=True)
    device_type = Column(String(256), nullable=True)
