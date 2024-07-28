# from fastapi import FastAPI, HTTPException, status, UploadFile, File, Form
# from core import config
from fastapi import FastAPI
from core import smtp as mailer
# from core.model import ResUserModel, ReqUserModel, BaseUserModel,LoginModel,RegisterModel
# from core.schema import UserTable, PapersTable
# import time

# from core.utility import getPassHash

# dbr = config.getDb()
app = FastAPI()

@app.get("/")
async def get_users():
    return {"messege":"its working 🚀 !"}

@app.get("/verify")
async def get_users():
    to_email = 'xa1244661@gmail.com'
    subject = 'Hello anon !'
    body = 'You are one step away to access all the features of ChatingPoint and connect with your friends and family and your gropu. you can discus your doubts and solve other doubt. Please click here to complete your registration. https://test-aniflicks.onrender.com'
    mailer.sendVerifyMail(to_email= to_email, subject= subject, body= body)
    return {"messege":"Verification link was sent."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2004, log_level="info")


# @app.get("/user/{id}", response_model=ResUserModel)
# def get_userBy_id(id: int):
#     user = dbr.query(UserTable).filter(UserTable.id == id).first()
#     if user == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No user found with id {id}")
#     return user


# @app.post("/user/register",response_model=RegisterModel, status_code=status.HTTP_201_CREATED)
# def create_user(userModel : ReqUserModel):
#     tkn = getPassHash(userModel.email+userModel.password)
#     user = dbr.query(UserTable).filter(UserTable.email == userModel.email).first()
#     if user != None:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"User with email {userModel.email} already exist !")
#     newUser = UserTable(name=userModel.name, email= userModel.email, password = userModel.password,token = tkn)
#     dbr.add(newUser)
#     dbr.commit()
#     dbr.refresh(newUser)
#     return newUser

# @app.post("/user/login")
# async def login(userDetail : LoginModel):
#     newToken = getPassHash(userDetail.email+userDetail.password)
#     result = dbr.query(UserTable).filter(UserTable.token == newToken).first()
#     if result == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Incorrect email or password")
#     return {"msg":"Loggin succesfull"}

# @app.get("/users", response_model=list[ResUserModel])
# def get_all_users() -> any:
#     userlist = dbr.query(UserTable).all()
#     return userlist

# @app.put("/user/{id}", response_model=ResUserModel)
# def update_user(id:int, updateModel:BaseUserModel):
#     user = dbr.query(UserTable).filter(UserTable.id == id)
#     if user.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} doesn't exist !")
    
#     if updateModel.name !=None:
#         if updateModel.email != None:
#             user.update(updateModel.model_dump())
#         else:
#             user.update({'name':f'{updateModel.name}'})
#     else:
#         if updateModel.email != None:
#             user.update({'email':f'{updateModel.email}'})
#     dbr.commit()
#     return user.first()

# @app.delete("/delete/{id}")
# def delete_user(id:int):
#     user = dbr.query(UserTable).filter(UserTable.id == id)
#     if user.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} doesn't exist !")
#     user.delete()
#     dbr.commit()
#     return {"msg":"User deleted succesfully !"}


# @app.post("/paper/upload")
# async def uploadFile(file : UploadFile = File() , year:str=Form() , sem: int=Form(), dept:str=Form(), sub : str=Form()):
#     filename : str = time.time()
#     filename = str(filename).split(".").pop()
#     fileExt = file.filename.split(".").pop()
#     filePath = f"files/{filename}.{fileExt}"
#     content = file.file.read()
#     fp = open(filePath, "wb")
#     fp.write(content)
#     newFile = PapersTable(file = filePath, year = year, sem = sem, dept = dept, sub = sub)
#     dbr.add(newFile)
#     dbr.commit()
#     dbr.refresh(newFile)
#     fp.close()
#     return {
#         "msg":"File uploaded succesfully !",
#         "details":newFile
#     }

# @app.get("/paper/find")
# async def getAllPapers():
#     allRecords = dbr.query(PapersTable).all()
#     return {"total":f"Total {len(allRecords)} papers found of all dept !","details":allRecords}

# @app.get("/paper/dept/find")
# async def papersOfDept(dept:str):
#     records = dbr.query(PapersTable).filter(PapersTable.dept == dept).all()
#     if records == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No records found !")
#     return records
