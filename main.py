from fastapi import FastAPI, HTTPException, status
from core import config
from core.model import ResUserModel, ReqUserModel, BaseUserModel
from core.schema import UserTable


dbr = config.getDb()
app = FastAPI()

@app.get("/")
async def get_users():
    return {"messege":"its working 🚀 !"}


@app.get("/user/{id}", response_model=ResUserModel)
def get_userBy_id(id: int):
    user = dbr.query(UserTable).filter(UserTable.id == id).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No user found with id {id}")
    return user


@app.post("/user", response_model=ResUserModel, status_code=status.HTTP_201_CREATED)
def create_user(userModel : ReqUserModel):
    user = dbr.query(UserTable).filter(UserTable.email == userModel.email).first()
    if user != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"User with email {userModel.email} already exist !")
    newUser = UserTable(name=userModel.name, email= userModel.email, password = userModel.password)
    dbr.add(newUser)
    dbr.commit()
    dbr.refresh(newUser)
    return newUser

@app.get("/users", response_model=list[ResUserModel])
def get_all_users() -> any:
    userlist = dbr.query(UserTable).all()
    return userlist

@app.put("/user/{id}", response_model=ResUserModel)
def update_user(id:int, updateModel:BaseUserModel):
    user = dbr.query(UserTable).filter(UserTable.id == id)
    if user.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} doesn't exist !")
    
    if updateModel.name !=None:
        if updateModel.email != None:
            user.update(updateModel.model_dump())
        else:
            user.update({'name':f'{updateModel.name}'})
    else:
        if updateModel.email != None:
            user.update({'email':f'{updateModel.email}'})
    dbr.commit()
    return user.first()

@app.delete("/delete/{id}")
def delete_user(id:int):
    user = dbr.query(UserTable).filter(UserTable.id == id)
    if user.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} doesn't exist !")
    user.delete()
    dbr.commit()
    return {"msg":"User deleted succesfully !"}