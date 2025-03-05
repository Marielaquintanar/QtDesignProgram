from pydantic import BaseModel

class Usuario(BaseModel):
    id: int | None = None
    nombre: str
    rol: str

    class Config:
        orm_mode = True