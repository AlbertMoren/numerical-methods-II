from pydantic import BaseModel

class DerivativeRequest(BaseModel):
    funcao: str
    x: float
    h: float
    metodo: str
    ordem: int