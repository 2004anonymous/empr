from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Url = "mysql+pymysql://root@localhost:3306/test"
Url = "postgresql://anonymous:V7p0qCcLybCGWED8VZVECAj6oJoAhHQL@dpg-cmd4ug821fec73d0a3mg-a.oregon-postgres.render.com/admin_db_ckfr"

engine = create_engine(url=Url)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print("Connection succesfull !")
Base = declarative_base()

def getDb():
    try:
        return session()
    except Exception as  er:
        session().close()
        return {"error":"Connection failed to database !"}
