from fastapi import APIRouter, HTTPException
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.get("/")
async def get_usuarios():
    return {"usuarios": ["Pablo", "Mariela"]}


@router.post('/')
async def create_usuario(usuario: Usuario):
    print(usuario)
    nuevo_usuario = await UsuarioDAO.create(usuario)
    if not nuevo_usuario:
        raise HTTPException(status_code=400, detail='No se pudo crear el usuario')
    return nuevo_usuario