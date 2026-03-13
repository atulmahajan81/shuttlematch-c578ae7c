from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from .routers import auth, user, tournament
from .config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)

@app.on_event("startup")
async def startup_event():
    """
    Actions to perform at startup.
    """
    # Initialize database connections, etc.

@app.on_event("shutdown")
async def shutdown_event():
    """
    Actions to perform at shutdown.
    """
    # Close database connections, cleanup, etc.

# Include routers
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(tournament.router)