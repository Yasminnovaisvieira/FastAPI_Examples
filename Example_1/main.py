from fastapi import FastAPI, HTTPException, status, Response, Depends # Se der erro: Coloque manualmente o python.exe dentro do Scripts
from models import PersonagensToyStory
from typing import Optional, Any
from routes import curso_router, user_router
import requests

app = FastAPI(title="API de Personagens de Toy Story - Yasmin Novais Vieira", version="0.0.1", description="Uma API feita para aprender Fast API")

app.include_router(curso_router.router, tags=["Cursos"]) #Solicitar uma rota que já existe e trabalhar em cima dela
app.include_router(user_router.router, tags=["Usuários"])


@app.get("/pokemon/{name}")
def get_pokemon(nome: str): # Não tem o async pois é uma função sincrona
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    if response.status_code == 200:
        return response.json()
    return {"Message" : "Pokemon not found"}


def fake_db():
    try:
        print("Conectando com o banco")
    finally:
        print("Fechando o banco")

personagens = {
    1: {
        "nome": "Woody",
        "dono": "Andy",
        "tamanho": "Pequeno",
        "foto": "https://media.tenor.com/NBzVDCUnp0oAAAAe/woody-smile.png"
    },
    2: {
        "nome": "Buzz Lighter",
        "dono": "Bonnie",
        "tamanho": "Pequeno",
        "foto": "https://us-tuna-sounds-images.voicemod.net/27771d97-42aa-4446-8541-dc0099264ec2-1691888427349.png"
    }
}


# @app.get("/")
# async def raiz():
#     return {"Mensagem" : "Hello, World!"}

# @app.get("/personagens")
# async def get_personagens(db: Any = Depends(fake_db)):
#     return personagens

# @app.get("/personagens/{personagem_id}", description="Retorna um personagem com um ID específico", summary="Retorna um personagem")
# async def get_personagem(personagem_id: int):
#     try:
#         personagem = personagens[personagem_id] 
#         return personagem
#     except KeyError:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Personagem não encontrado"
#         )

# @app.post("/personagens", status_code=status.HTTP_201_CREATED)
# async def post_personagem(personagem: Optional[PersonagensToyStory] = None):
#     next_id = len(personagens) + 1
#     personagens[next_id] = personagem
#     del personagem.id # Quando for visualizar o JSON para que não apareça 2 IDs
#     return personagem

# @app.put("/personagens/{personagem_id}", status_code=status.HTTP_202_ACCEPTED)
# async def put_personagem(personagem_id:int, personagem: PersonagensToyStory):
#     if personagem_id in personagens:
#         personagens[personagem_id] = personagem
#         personagem.id = personagem_id
#         del personagem_id
#         return personagem
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Personagem não encontrado"
#         )
    
# @app.delete("/personagens/{personagem_id}")
# async def delete_personagem(personagem_id: int):
#     if personagem_id in personagens:
#         del personagens[personagem_id]
#         return Response(status_code=status.HTTP_204_NO_CONTENT)
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Personagem não encontrado"
#         )
    
# app.get("/calcular")
# async def calcular(a:int, b:int):
#     soma = a + b
#     return {"Resultado": soma}

# Vai rodar o servidor automaticamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host = "127.0.0.1", port = 8001, log_level = "info", reload = True)