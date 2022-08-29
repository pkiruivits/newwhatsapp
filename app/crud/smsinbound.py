from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import smsinbound as smsinboundmodel #models
from app.schemas import smsinbound as smsinboundschema #models
from sqlalchemy import select, update
from fastapi.encoders import jsonable_encoder
import http.client
import json
#from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(smsinboundmodel.User).filter(smsinboundmodel.User.id == user_id).first()

async def get_sms_by_id(db: AsyncSession, sms_id: str):
    result = await db.execute(
            select(smsinboundmodel.SmsInbound)
            .filter(smsinboundmodel.SmsInbound.sms_id==sms_id)
             )
    await db.commit()
    return result.scalars().one()
    

def get_user_by_email(db: Session, email: str):
    return db.query(smsinboundmodel.User).filter(smsinboundmodel.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(smsinboundmodel.User).offset(skip).limit(limit).all()


async def create_inbound(db: Session, smsinbound: smsinboundschema.smsinboundCreate,commit=True):

    obj_in_data = jsonable_encoder(smsinbound, exclude_unset=True)
    db_smsinbound = smsinboundmodel.SmsInbound(**obj_in_data)
    db.add(db_smsinbound)
    if commit:
        await db.commit()
    else:
        await db.flush()
    

    return db_smsinbound
    

async def get_inbounds(db: AsyncSession, skip: int = 0, limit: int = 100)-> List[smsinboundmodel.SmsInbound]:
        result = await db.execute(
            select(smsinboundmodel.SmsInbound)
            .offset(skip)
            .limit(limit)
        )
        await db.commit()
        return result.scalars().all()

async def get_all_waiting(db: AsyncSession, limit: int = 100):
    result = await db.execute(
            select(smsinboundmodel.SmsInbound).filter(smsinboundmodel.SmsInbound.replied==False).limit(limit)
        )
    await db.commit()
    return result.scalars().all()

async def sentsms(tokenstr:str,phone:str,message:str,prevsmsid:str):
    ''' sms body object
    {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": "{{Recipient-Phone-Number}}",
    "context": {
        "message_id": "<MSGID_OF_PREV_MSG>"
    },
    "type": "text",
    "text": {
        "preview_url": false,
        "body": "<TEXT_MSG_CONTENT>"
    }
}'''
    print("reached sent sms",phone)
    bodyobj={
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": phone,
    "context": {
        "message_id": prevsmsid
    },
    "type": "text",
    "text": {
        "preview_url": False,
        "body": message
    }
    }
    conn = http.client.HTTPSConnection("graph.facebook.com")
    payload1 = json.dumps(bodyobj)
    payload = json.dumps({
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": "{{phone}}",
    "context": {
        "message_id": "{{prevsmsid}}"
    },
    "type": "text",
    "text": {
        "preview_url": False,
        "body": "{{message}}"
    }
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+tokenstr
    }
    print
    print(payload1,headers)
    conn.request("POST", "/v14.0/103570139153202/messages", payload1, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))#
    return payload

async def update_sent(db:AsyncSession,msg_id:str):
    
    data = {smsinboundmodel.SmsInbound.replied: True}
    #obj_in_data = jsonable_encoder(data, exclude_unset=True)
    try:
        result = await db.execute(
                update(smsinboundmodel.SmsInbound)
                .filter(
                    smsinboundmodel.SmsInbound.sms_id==msg_id
                ).values(data)
                #.filter_by(**kwargs)
            )
        await db.execute("commit")
    except Exception as e: 
        print("Error Found",e)
    
    await db.flush()
    
