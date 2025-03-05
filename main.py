from fastapi import FastAPI
from controllers.usuario_controller import router as usuario_router

app = FastAPI()

# Registrar rutas
app.include_router(usuario_router)

@app.get("/")
async def root():
    return {"message": "Servidor corriendo"}
