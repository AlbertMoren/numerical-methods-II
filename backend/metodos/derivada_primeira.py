import math
from fastapi import HTTPException

class DerivadaPrimeira:
    def __init__(self,funcao: str,x:float,h: float):
        self.funcao = funcao
        self.x = x
        self.h = h
    
    def _avaliar(self, valor_x: float) -> float:
        ambiente_seguro = {"x": valor_x, "math": math}
        try:
            return eval(self.funcao, {"__builtins__": {}},ambiente_seguro)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao avaliar função: {e}")

    def calcular_forward(self) -> float:
        fx = self._avaliar(self.x)
        fx_mais_h = self._avaliar(self.x + self.h)
        return (fx_mais_h - fx) / self.h

    def calcular_backward(self) -> float:
        fx = self._avaliar(self.x)
        fx_menos_h = self._avaliar(self.x - self.h)
        return (fx - fx_menos_h) / self.h

    def calcular_central(self) -> float:
        fx_mais_h = self._avaliar(self.x + self.h) 
        fx_menos_h = self._avaliar(self.x - self.h)
        return (fx_mais_h - fx_menos_h) / (2*self.h)