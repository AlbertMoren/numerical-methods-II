from fastapi import FastAPI, HTTPException
from backend.models import DerivativeRequest
from backend.metodos.derivada_primeira import DerivadaPrimeira

app = FastAPI()

@app.post("/derivar")
def calcular_derivada(req: DerivativeRequest):
    if req.ordem == 1:
        calculadora = DerivadaPrimeira(req.funcao,req.x,req.h)

        if req.metodo == "forward":
            resultado = calculadora.calcular_forward()
        elif req.metodo == "backward":
            resultado = calculadora.calcular_backward()
        elif req.metodo == "central":
            resultado = calculadora.calcular_central()
        else:
            raise HTTPException(status_code=400,detail="Método Inválido")
        
        return {"resultado": resultado, "metodo": req.metodo, "ordem":req.ordem}
    raise HTTPException(status_code=501, detail="Ordens 2 e 3 ainda não foram impĺementadas.")
    