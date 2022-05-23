from api import db
from sqlalchemy.sql import func
import datetime

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(150),unique=True,nullable=False)
    content = db.Column(db.String(100000),nullable=False)
    date_created = db.Column(db.String,default=datetime.datetime.utcnow().strftime('%B %d %Y'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title':self.title,
            'content':self.content,
            'date_created':self.date_created,
        }
