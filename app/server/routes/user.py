from fastapi import Body, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasicCredentials
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
from app.server.auth.user import validate_login
from app.server.auth.jwt_handler import signJWT
from app.server.database.database import *
from app.server.models.user import *

router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])

@router.post("/login")
async def user_login(user: HTTPBasicCredentials = Body(...)):
	if validate_login(user):
		return {
			"email": user.username,
			"access_token": signJWT(user.username)
		}
	return "Invalid Login Details!"

@router.post("/signup")
async def user_signup(user: UserModel = Body(...)):
	# TODO: Perform validation to check if user exists.
	user.password = hash_helper.encrypt(user.password)
	new_user= await add_user(jsonable_encoder(user))
	return new_user

@router.get("/list", response_description="Users retrieved")
async def users_list():
	users = await retrieve_users()
	lists = jsonable_encoder(users)
	if len(users) > 0:
		return JSONResponse(content=lists)
	else:
		return "Empty list"