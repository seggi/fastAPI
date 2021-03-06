from typing import List
from fastapi import APIRouter



from fastapi import APIRouter , Body, Depends
from starlette.status import HTTP_201_CREATED

from app.models.cleaning import CleaningCreate, CleaningPublic
from app.db.repositories.cleanings import CleaningsRepository
from app.api.dependencies.database import get_repository


auth = APIRouter()

@auth.get("/")
async def get_all_auth() -> List[dict]:
	users = [{"id": 1, "name": "Kona"}]
	return users

@auth.post("/", response_model=CleaningPublic, name="cleanings:create-cleaning", status_code=HTTP_201_CREATED)
async def create_new_cleaning(
    new_cleaning: CleaningCreate = Body(..., embed=True),
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),
	) -> CleaningPublic:
    created_cleaning = await cleanings_repo.create_cleaning(new_cleaning=new_cleaning)
    return created_cleaning