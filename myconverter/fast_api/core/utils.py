from functools import wraps

import aiohttp
from fastapi import HTTPException
from db.keycloak import KEYCLOAK_URL

from core.config import AUTH_REQUIRED


async def request(session):
    async with session.get(KEYCLOAK_URL) as response:
        return await response.text()


def check_auth(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        authorization = kwargs['authorization']
        if AUTH_REQUIRED:
            if not authorization or 'Bearer' not in authorization:
                raise HTTPException(status_code=401, detail="Unauthorized")
            headers = {'Authorization': authorization}
            async with aiohttp.ClientSession(headers=headers) as session:
                result = await request(session)
                if 'sub' not in result:
                    raise HTTPException(status_code=401, detail="Unauthorized")
        return await func(*args, **kwargs)
    return inner
