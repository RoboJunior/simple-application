from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="Simple Application")


# Home route
@app.route("/")
async def home(request: Request):
    return JSONResponse(
        content={
            "message": f"Request coming from Host: {request.client.host} Port: {request.client.port}"
        },
        status_code=200,
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="app.main:app", host="0.0.0.0", port=8003)
