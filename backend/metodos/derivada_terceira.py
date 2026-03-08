import math
from fastapi import HTTPException

class DerivadaTerceira:
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
        fx_mais_1 = self._avaliar(self.x + self.deltaX)
        fx_mais_2 = self._avaliar(self.x + 2 * self.deltaX)
        fx_mais_3 = self._avaliar(self.x + 3 * self.deltaX)
        return (fx_mais_3 - 3 * fx_mais_2 + 3 * fx_mais_1 - fx) / (self.deltaX ** 3)

    def calcular_backward(self) -> float:
        fx = self._avaliar(self.x)
        fx_menos_1 = self._avaliar(self.x - self.deltaX)
        fx_menos_2 = self._avaliar(self.x - 2 * self.deltaX)
        fx_menos_3 = self._avaliar(self.x - 3 * self.deltaX)
        return (fx - 3 * fx_menos_1 + 3 * fx_menos_2 - fx_menos_3) / (self.deltaX ** 3)
    
    def calcular_central(self) -> float:
        fx_mais_2 = self._avaliar(self.x + 2 * self.deltaX)
        fx_mais_1 = self._avaliar(self.x + self.deltaX)
        fx_menos_1 = self._avaliar(self.x - self.deltaX)
        fx_menos_2 = self._avaliar(self.x - 2 * self.deltaX)
        return (fx_mais_2 - 2 * fx_mais_1 + 2 * fx_menos_1 - fx_menos_2) / (2 * (self.deltaX ** 3))