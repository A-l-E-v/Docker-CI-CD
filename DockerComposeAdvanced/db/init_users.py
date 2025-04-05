import sys
import os

# Добавляем /app в PYTHONPATH, так как backend монтируется в /app
sys.path.append('/app')

from base import Base, engine, User, SessionLocal

def init_data():

	Base.metadata.create_all(bind=engine)

	users = [
    	User(login='pavel', email='a@gmail.com'),
    	User(login='yura', email='b@gmail.com')
	]

	db = SessionLocal()

	for user in users:
    		db.add(user)
	db.commit()

if __name__ == "__main__":
    init_data()
