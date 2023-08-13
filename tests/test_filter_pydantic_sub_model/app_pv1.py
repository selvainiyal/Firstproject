from typing import Optional

from fastapi import Depends, FastAPI
<<<<<<< HEAD
from pydantic import BaseModel, validator
=======
from pydantic import BaseModel
>>>>>>> a1c1fa61f06a55ee077e7fa1c980d1eceb698091

app = FastAPI()


class ModelB(BaseModel):
    username: str


class ModelC(ModelB):
    password: str


class ModelA(BaseModel):
    name: str
    description: Optional[str] = None
    model_b: ModelB

    @validator("name")
    def lower_username(cls, name: str, values):
        if not name.endswith("A"):
            raise ValueError("name must end in A")
        return name


async def get_model_c() -> ModelC:
    return ModelC(username="test-user", password="test-password")


@app.get("/model/{name}", response_model=ModelA)
async def get_model_a(name: str, model_c=Depends(get_model_c)):
    return {"name": name, "description": "model-a-desc", "model_b": model_c}
