import re
import math

def traduzir_para_python(expressao: str) -> str:
    expr = expressao.replace(" ", "")
    expr = re.sub(r'(\d)([a-zA-Z\(])', r'\1*\2', expr)
    expr = expr.replace("^","**")
    expr = expr.replace("π", "math.pi")
    expr = expr.replace("pi", "math.pi")
    
    expr = re.sub(r'(?<![a-zA-Z])e(?![a-zA-Z])', 'math.e', expr)
    
    funcoes_math = {
        "sen": "math.sin", "sin": "math.sin", "cos": "math.cos",
        "tan": "math.tan", "sqrt": "math.sqrt", "log": "math.log",
        "exp": "math.exp"
    }

    for humano, python in funcoes_math.items():
        expr = expr.replace(humano, python)

    expr = expr.replace("math.math.", "math.")
    return expr