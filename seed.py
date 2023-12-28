from app import app
from models import db, User, Feedback, connect_db

connect_db(app)
db.drop_all()
db.create_all()

a =User.register(pwd = "this",username="alextreyes", email = "alex@gmail.com", fname = "Alex", lname= "Reyes")
post1 = Feedback(title="this1", content='that1', username='alextreyes')
post2 = Feedback(title="this2", content='that2', username='alextreyes')

posts = [post1,post2]
db.session.add(a)
db.session.commit()
db.session.add_all(posts)
db.session.commit()