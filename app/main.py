from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api import statistics
from app.core.utils import CustomException

app = FastAPI()
app.include_router(statistics.router, prefix="/api", tags=["statistics"])


@app.exception_handler(CustomException)
async def unicorn_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"details": exc.name}
    )
