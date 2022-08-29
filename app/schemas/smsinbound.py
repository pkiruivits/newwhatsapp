from typing import List, Optional
from datetime import datetime, date
from pydantic import BaseModel

class smsinboundBase(BaseModel):
    Request_id: str
    display_phone: str
    phone_no_id: str
    contact_name: str
    contact_wa_id: str
    sms_id: str
    type: str
    text_body: str
    replied: bool=False
    #created_at: Optional[datetime]
   

class smsinboundCreate(smsinboundBase):
    pass

class SmsInbound(smsinboundBase):
    id: int

    class Config:
        orm_mode = True
