import math
from fastapi import HTTPException

class DerivadaPrimeira:
    def __init__(self,funcao: str,x:float,deltaX: float):
        self.funcao = funcao
        self.x = x
        self.deltaX = deltaX
    
    def _avaliar(self, valor_x: float) -> float:
        ambiente_seguro = {"x": valor_x, "math": math}
        try:
            return eval(self.funcao, {"__builtins__": {}},ambiente_seguro)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao avaliar função: {e}")

    def calcular_forward(self) -> float:
        fx = self._avaliar(self.x)
        fx_mais_deltaX = self._avaliar(self.x + self.deltaX)
        return (fx_mais_deltaX - fx) / self.deltaX

    def calcular_backward(self) -> float:
        fx = self._avaliar(self.x)
        fx_menos_deltaX = self._avaliar(self.x - self.deltaX)
        return (fx - fx_menos_deltaX) / self.deltaX

    def calcular_central(self) -> float:
        fx_mais_deltaX = self._avaliar(self.x + self.deltaX) 
        fx_menos_deltaX = self._avaliar(self.x - self.deltaX)
        return (fx_mais_deltaX - fx_menos_deltaX) / (2*self.deltaX)