from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Subscription(Base):
  __tablename__ = 'subscriptions'

  id = Column(Integer, primary_key=True)
  email = Column(String(120), unique=True)
  created_at = Column(DateTime) # utcnow

  def __init__(self, email, created_at=None):
    self.email = email
    if created_at == None:
      created_at = datetime.utcnow()
    self.created_at = created_at

  def __repr__(self):
    return '<Subscription %r>' % self.email