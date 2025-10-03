from fastapi import FastAPI
from app.database.migration import init_db
from app.api.user import router as outfit
from scalar_fastapi import get_scalar_api_reference
from app.api.auth import authentication as auth_router



app = FastAPI(
    title="Fashion Outfit API",
    description="Fashion Outfit API",
    version="1.0",
)


app.include_router(outfit)
app.include_router(auth_router)

@app.on_event("startup")
async def startup_event():
    init_db()


@app.get("/scalar")
def get_scalar_doc():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="FastAPI with Scalar"
    )
