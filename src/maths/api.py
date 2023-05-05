from fastapi import FastAPI
import os, uvicorn
from typing import List, Literal
from pydantic import BaseModel

# CONFIG
app = FastAPI(
    title="Math Tool",
    version="0.0.1",
    description="This API with do simple math operations",
)

# API INPUT
class Input(BaseModel):
    """Modeling of one input data in a type-restricted dictionary-like format

    column_name : variable type # strictly respect the name in the dataframe header.

    eg.:
    =========
    customer_age : int
    gender : Literal['male', 'female', 'other']
    """

    x: float
    y: float


# ENDPOINTS

## Status endpoint : check if the api is online
@app.get("/status")
async def status():
    return {"message": "online"}

## Addition with structured input
@app.post("/add")  #  # the string in the post methode is the endpoint link
async def operation(input: Input):
    "Function that receive the posted input data, do the operation and return an output/error message"
    output = {}  # None

    # try to execute the operation loop
    try:
        result = input.x + input.y

        # format output
        output = {
            "result": result,
            "operation": "addition",
            "way": "sending parameters as a payload",
            "x": input.x,
            "y": input.y,
        }

    except ValueError as e:
        output = {"error": str(e)}

    except Exception as e:
        output = {"error": f"Oops something went wrong:\n{e}"}

    finally:
        return output  # output must be json serializable


## Addition with input coming from the link/url
@app.get("/add/{a}_{b}")  #  # the string in the post methode is the endpoint link
async def operation(a:float, b:float):
    "Function that receive the posted input data, do the operation and return an output/error message"
    output = {}  # None

    # try to execute the operation loop
    try:
        result = a + b
        # result = float(a) + float(b)

        # format output
        output = {
            "result": result,
            "operation": "addition",
            "way": "Sending parameters by path/URL",
            "x": a,
            "y": b,
        }

    except ValueError as e:
        output = {"error": str(e)}

    except Exception as e:
        output = {"error": f"Oops something went wrong:\n{e}"}

    finally:
        return output  # output must be json serializable



if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)
