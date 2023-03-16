from app.models import User, Post, Comment, Vote
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

#insert posts
db.add_all([
  Post(title='Python 3.11.2, Python 3.10.10 and 3.12.0 alpha 5 are available', post_url='https://pythoninsider.blogspot.com/2023/02/python-3112-python-31010-and-3120-alpha.html', user_id=1),
  Post(title='Python News', post_url='https://realpython.com/python-news-october-2022/', user_id=1),
  Post(title='Go re-enters TIOBE’s top 10 programming languages', post_url='https://www.developer-tech.com/news/2023/mar/14/go-reenters-tiobe-top-10-programming-languages/', user_id=2),
  Post(title='The digital engineering revolution is here — could Python be the key to upskilling?', post_url='https://thenextweb.com/news/digital-engineering-could-python-key-to-upskilling', user_id=3),
  Post(title='Python Packaging Strategy Discussion Summary - Part 1', post_url='https://pyfound.blogspot.com/2023/02/python-packaging-strategy-discussion.html', user_id=4)
])
db.commit()

# insert comments
db.add_all([
  Comment(comment_text='Comment 1', user_id=1, post_id=2),
  Comment(comment_text='Comment 2', user_id=1, post_id=3),
  Comment(comment_text='Comment 3', user_id=2, post_id=1),
  Comment(comment_text='Comment 4', user_id=2, post_id=3),
  Comment(comment_text='Comment 5', user_id=3, post_id=3)
])

db.commit()

# insert votes
db.add_all([
  Vote(user_id=1, post_id=3),
  Vote(user_id=1, post_id=3),
  Vote(user_id=2, post_id=4),
  Vote(user_id=3, post_id=2),
  Vote(user_id=4, post_id=4)
])

db.commit()

db.close()