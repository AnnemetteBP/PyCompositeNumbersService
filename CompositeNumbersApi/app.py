from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from CompositeNumbersClass import CompositeNumbers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

composite_numbers_client = CompositeNumbers()

@app.on_event("startup")
async def startup():
    print("App is running...")

@app.on_event("shutdown")
async def shutdown():
    print("App is shutting down...")

@app.get("/check_number/", status_code=200)
async def check_number(number: int) -> bool:
    try:
        check_number_result = composite_numbers_client.check_number(number)
    except Exception as e:
        check_number_result = None
        Response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return check_number_result

@app.get("/check_numbers_list/", status_code=200)
async def check_numbers_list(num1: int, num2: int) -> list:
    try:
        composite_numbers_result = composite_numbers_client.check_numbers_list(num1, num2)
    except Exception as e:
        composite_numbers_result = None
        Response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return composite_numbers_result