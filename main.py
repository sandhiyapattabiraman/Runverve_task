from fastapi import FastAPI
from contextlib import asynccontextmanager
from modules.utils.database import create_db_and_tables
from modules.user.user_controller import user_router
from modules.user_matrix.user_matrix_controller import matrix_router
from modules.product.product_controller import device_router



@asynccontextmanager
async def lifespan(app):
       create_db_and_tables()
       yield
 
app = FastAPI(title="project", lifespan=lifespan)     

app.include_router(router=user_router)
app.include_router(router=matrix_router)
app.include_router(router=device_router)


@app.get("/")
def initial_route(): 
    return {"message" : "Hello World"}
