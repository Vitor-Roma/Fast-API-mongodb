from fastapi import FastAPI
import router

app = FastAPI()


@app.get('/')
async def Home():
    return 'teste'


app.include_router(router.router)
