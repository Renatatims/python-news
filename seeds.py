from app.models import User
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
  User(username='user0', email='user0@gmail.com', password='user0pass123'),
  User(username='user1', email='user1@gmail.com', password='user1pass123'),
  User(username='user2', email='user2@gmail.com', password='user2pass123'),
  User(username='user3', email='user3@gmail.com', password='user3pass123'),
  User(username='user4', email='user4@gmail.com', password='user4pass123')
])

db.commit()

db.close()