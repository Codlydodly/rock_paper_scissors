from fastapi import HTTPException, status
from database.query import DatabaseConnector
from auth.provider import AuthProvider
from user.models import UserUpdateRequestModel

database = DatabaseConnector()

def createUser(userModel: UserCreateRequestModel) -> int:
    print(userModel)


def updateUser(user_model: UserUpdateRequestModel) -> int:
    existingUser =