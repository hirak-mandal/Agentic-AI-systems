from fastapi import FastAPI
from api.chat import router

#create main FastAPI application/server instance
app=FastAPI()

#connect routes to app
app.include_router(router)

    