import uvicorn
from fastapi import FastAPI

from routes.dataGetting import dataGetting
from routes.linearFitting import linearFitting

# Main API
app = FastAPI(title='ML API',
              description= "To be python backend service for ML app",
              version="0.0.1",
              )

@app.get("/")
async def main():
    return {"message": "Hello Main ML API by FastAPI =>See the API document in host*/docs"}

# Sub API (Router)
app.include_router(dataGetting)
app.include_router(linearFitting)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)