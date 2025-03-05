from database.connection import supabase
from models.usuario import Usuario

class UsuarioDAO:
    @staticmethod
    async def get_all():
        response = supabase.table("usuarios").select("*").execute()
        return response.data

    @staticmethod
    async def get_by_id(user_id: int):
        response = supabase.table("usuarios").select("*").eq("id", user_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    async def create(usuario: Usuario):
        usuario_dict = usuario.model_dump(exclude={"id"})
        response = supabase.table("usuario").insert(usuario_dict).execute()
        return response.data[0] if response.data else None

    @staticmethod
    async def delete(user_id: int):
        response = supabase.table("usuarios").delete().eq("id", user_id).execute()
        return response.data
