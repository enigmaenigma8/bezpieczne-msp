"""
Główny punkt wejścia FastAPI (szkielet).
"""

from fastapi import FastAPI

app = FastAPI(title="Bezpieczne MSP", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}
