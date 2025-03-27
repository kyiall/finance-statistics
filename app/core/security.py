from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt

from app.core.config import settings
from app.core.utils import CustomError

security = HTTPBearer()


async def get_current_user(
        credentials: HTTPAuthorizationCredentials = Security(security)
):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise CustomError(status_code=401, name="No User")
        return user_id
    except jwt.ExpiredSignatureError:
        raise CustomError(status_code=401, name="Token expired")
    except jwt.JWTError:
        raise CustomError(status_code=401, name="Invalid token 2")
