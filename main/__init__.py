from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from main.config import config


app = FastAPI(title=config.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def run():
    from main.controllers import controller_router

    @controller_router.get("/")
    async def root():
        return {"status": "Fine"}

    app.include_router(router=controller_router)


run()
