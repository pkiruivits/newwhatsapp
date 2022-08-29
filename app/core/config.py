import secrets
from typing import Any, Dict, List, Optional, Union
from xxlimited import Str

from pydantic import (
    AnyHttpUrl, 
    BaseSettings, 
    EmailStr, 
    HttpUrl, 
    validator,
    SecretStr
)


from dotenv import load_dotenv

from urllib.parse import urlencode

from dataclasses import dataclass,InitVar



load_dotenv()


class Settings(BaseSettings):
    DEBUG: bool
    #API_V1_STR: str
    SECRET_KEY: SecretStr
    PROJECT_NAME: str
    PROJECT_DOMAIN: str    
    REDIS_URL: str
    #tokens
    WHATSAPP_API_TOKEN:str
    SESSION_COOKIE_EXPIRE_MINUTES: int = 60

    ADMIN_SESSION_COOKIE_EXPIRE_MINUTES: int = 60

    PORTAL_SESSION_COOKIE_EXPIRE_MINUTES: int = 600


    #tokens
    EMAIL_RESET_TOKEN_EXPIRE_MINUTES: int = 60
    #EMAIL_ACTIVATION_TOKEN_EXPIRE_MINUTES: int = 60
    ACCOUNT_VERIFICATION_CODE_EXPIRE_MINUTES: int = 3600

    SMTP_HOST = 'smtp.gmail.com'
    SMTP_EMAIL_SENDER: str
    SMTP_EMAIL_PASSWORD: str
    EMAILS_ENABLED=True
    SMTP_PORT=465
    #SMTP_USER=SMTP_EMAIL_SENDER
    #SMTP_PASSWORD=SMTP_EMAIL_PASSWORD
    SMTP_TLS=False
    EMAILS_FROM_NAME: str

    DIGITAL_OCEAN_SPACES_KEY: str
    DIGITAL_OCEAN_SPACES_SECRET: str
    DIGITAL_OCEAN_SPACES_ENDPOINT_DOMAIN: str
    DIGITAL_OCEAN_SPACES_CDN_DOMAIN: str

    #the bucket hosts things like logos e.t.c
    DIGITAL_OCEAN_SPACES_PUBLIC_BUCKET_NAME: str

    ALLOWED_ORIGINS: List[str]

    ASYNC_DATABASE_URL: str

    EMAIL_TEMPLATES_DIR: str
    ACCOUNT_ACTIVATION_URL: str
    TEST_EMAIL: EmailStr

    


    class Config:
        case_sensitive = True


settings = Settings()