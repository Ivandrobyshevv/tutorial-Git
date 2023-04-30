import uuid

from config import database
from src.models import Animal


class AnimalRepo:

    @staticmethod
    async def retrieve():
        _animal = []
        collection = database.get_collection('animal').find()
        async for animal in collection:
            _animal.append(animal)
        return _animal

    @staticmethod
    async def insert(animal: Animal):
        _id = str(uuid.uuid4())
        birthday = f'{animal.birthday.day}.{animal.birthday.month}.{animal.birthday.year}'
        _animal = {
            '_id': _id,
            'name': animal.name,
            'birthday': birthday,
            'commands': animal.commands,
            'genus_name': animal.genus_name
        }
        await database.get_collection('animal').insert_one(_animal)

    @staticmethod
    async def update(_id: str, commands: str):
        _animal = await database.get_collection('animal').find_one({"_id": _id})
        _animal['commands'] = commands
        await database.update_collection('animal').update_one({"_id": _id}, {"$set": _animal})

    @staticmethod
    async def retrieve_id(_id: str):
        return await database.get_collection('animal').find_one({"_id": _id})

    @staticmethod
    async def delete(_id: str):
        await database.get_collection('animal').delete_one({"_id": _id})
