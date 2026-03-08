from pydantic import BaseModel

class DerivativeRequest(BaseModel):
    funcao: str
    x: float
    deltaX: float
    metodo: str
    ordem: int