from fastapi import FastAPI
from routes.routes import router

app = FastAPI()

# Include routers
app.include_router(router)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
