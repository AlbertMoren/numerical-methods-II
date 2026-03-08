from fastapi import FastAPI, HTTPException
from backend.models import DerivativeRequest
from backend.metodos.derivada_primeira import DerivadaPrimeira
from backend.metodos.derivada_segunda import DerivadaSegunda
from backend.metodos.derivada_terceira import DerivadaTerceira
app = FastAPI()

@app.post("/derivar")
def calcular_derivada(req: DerivativeRequest):
    if req.ordem == 1:
        calculadora = DerivadaPrimeira(req.funcao, req.x, req.deltaX)

        if req.metodo == "forward":
            resultado = calculadora.calcular_forward()
        elif req.metodo == "backward":
            resultado = calculadora.calcular_backward()
        elif req.metodo == "central":
            resultado = calculadora.calcular_central()
        else:
            raise HTTPException(status_code=400,detail="Método Inválido")
        
    elif req.ordem == 2:
        calculadora = DerivadaSegunda(req.funcao, req.x, req.deltaX)
        if req.metodo == "forward":
            resultado = calculadora.calcular_forward()
        elif req.metodo == "backward":
            resultado = calculadora.calcular_backward()
        elif req.metodo == "central":
            resultado = calculadora.calcular_central()
        else:
            raise HTTPException(status_code=400,detail="Método Inválido")
    
    elif req.ordem == 3:
        calculadora = DerivadaTerceira(req.funcao, req.x, req.deltaX)
        if req.metodo == "forward":
            resultado = calculadora.calcular_forward()
        elif req.metodo == "backward":
            resultado = calculadora.calcular_backward()
        elif req.metodo == "central":
            resultado = calculadora.calcular_central()
        else:
            raise HTTPException(status_code=400,detail="Método Inválido")
    
    if resultado is not None:
        return {"resultado": resultado, "metodo": req.metodo, "ordem": req.ordem}
        
    raise HTTPException(status_code=501, detail="Ordens 2 e 3 ainda não foram impĺementadas.")
    