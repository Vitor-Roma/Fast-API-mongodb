from fastapi import APIRouter, Request
from repository import CollectionRepo

router = APIRouter()


@router.get('/{collection}')
async def all_books(collection: str):
    return CollectionRepo(collection=collection).list()


@router.post('/{collection}')
async def create(request: Request, collection: str):
    _json = await request.json()
    item = CollectionRepo(collection=collection, _json=_json).create()
    return item


@router.get('/{collection}/{_id}')
def detail(collection: str, _id: str):
    return CollectionRepo(collection=collection, _id=_id).detail()


@router.delete('/{collection}/{_id}')
def delete(collection: str, _id: str):
    CollectionRepo(collection=collection, _id=_id).delete()
    return {"deleted": ''}


@router.patch('/{collection}/{_id}')
async def update(request: Request, collection: str, _id: str):
    _json = await request.json()
    CollectionRepo(collection=collection, _id=_id, _json=_json).update()
    return {"edited": _json}
