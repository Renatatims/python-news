from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt
salt = bcrypt.gensalt()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

  #Email - validate method - uses the assert keyword to check if an email address contains "@"
  @validates('email')
  def validate_email(self, key, email):
    # make sure email address contains @ character
    assert '@' in email
    return email
  
  #Password - Validate method - uses the assert to check the password's length
  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 4
    # encrypt password
    return bcrypt.hashpw(password.encode('utf-8'), salt)
  
  # Verify Password
  def verify_password(self, password):
   return bcrypt.checkpw(
     password.encode('utf-8'),
     self.password.encode('utf-8')
   )