from typing import Optional

from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials

from errors import TokenRequiredExc
from config import Config


class TokenDepends(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        return super().__init__(auto_error=auto_error)
    
    async def __call__(
        self, 
        request: Request,
    ) -> Optional[HTTPAuthorizationCredentials]:
        try:
            creds = await super().__call__(request)
        except HTTPException:
            raise TokenRequiredExc()
        token = creds.credentials
        if token is None or token != Config.BEARER_TOKEN:
            raise TokenRequiredExc()
        return token