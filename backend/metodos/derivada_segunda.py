import math
from fastapi import HTTPException

class DerivadaSegunda:
    def __init__(self, funcao: str, x: float, deltaX: float):
        self.funcao = funcao
        self.x = x
        self.deltaX = deltaX
    
    def _avaliar(self, valor_x: float) -> float:
        ambiente_seguro = {"x":valor_x, "math":math}
        try:
            return eval(self.funcao, {"__builtins__": {}},ambiente_seguro)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao avaliar função: {e}")
    
    def calcular_forward(self) -> float:
        fx = self._avaliar(self.x)
        fx_mais_1_deltaX  = self._avaliar(self.x + self.deltaX)
        fx_mais_2_deltaX  = self._avaliar(self.x + 2 * self.deltaX)
        return (fx_mais_2_deltaX - 2 * fx_mais_1_deltaX + fx) / (self.deltaX ** 2)
    
    def calcular_backward(self) -> float:
        fx = self._avaliar(self.x)
        fx_menos_1_deltaX = self._avaliar(self.x - self.deltaX)
        fx_menos_2_deltaX = self._avaliar(self.x - 2 * self.deltaX)
        return (fx - 2 * fx_menos_1_deltaX + fx_menos_2_deltaX) / (self.deltaX ** 2)
    
    def calcular_central(self) -> float:
        fx_mais_deltaX = self._avaliar(self.x + self.deltaX)
        fx = self._avaliar(self.x)
        fx_menos_deltaX = self._avaliar(self.x - self.deltaX)
        return (fx_mais_deltaX - 2 * fx + fx_menos_deltaX) / (self.deltaX ** 2)