from fastapi.routing import APIRoute

from src.crud import AnimalRepo
from src.models import Response, Animal


async def get_animals():
    _animals_list = await AnimalRepo.retrieve()
    return Response(code=200, status="Ok", message="Success retrieve all data", result=_animals_list).dict(
        exclude_none=True)


async def create_animal(animal: Animal):
    await AnimalRepo.insert(animal)
    return Response(code=200, status="Ok", message="Success save data").dict(exclude_none=True)


async def get_animal_by_id(_id: str):
    _animal = await AnimalRepo.retrieve_id(_id)
    return Response(code=200, status="Ok", message="Success retrieve data", result=_animal).dict(exclude_none=True)


async def animal_update(): pass


async def animal_delete(): pass


routes = [
    APIRoute(path="/animals", endpoint=get_animals, methods=["GET"]),
    APIRoute(path="/animal", endpoint=create_animal, methods=["POST"]),
    APIRoute(path="/animal/{id}", endpoint=get_animal_by_id, methods=["GET"]),
    APIRoute(path="/animal/update", endpoint=animal_update, methods=['PUT']),
    APIRoute(path="/animal/delete", endpoint=animal_delete, methods=['DELETE']),
]
