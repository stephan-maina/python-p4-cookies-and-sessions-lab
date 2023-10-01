from flask import Flask
from app import db, BlogPost

# Create an application context
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # SQLite database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy app with the application context
db.init_app(app)

def seed_database():
    with app.app_context():
        db.create_all()

        post1 = BlogPost(title="Post 1", content="Content of Post 1")
        post2 = BlogPost(title="Post 2", content="Content of Post 2")
        post3 = BlogPost(title="Post 3", content="Content of Post 3")
        post4 = BlogPost(title="Post 4", content="Content of Post 4")
        post5 = BlogPost(title="Post 5", content="Content of Post 5")

        db.session.add_all([post1, post2, post3, post4, post5])
        db.session.commit()

if __name__ == "__main__":
    seed_database()
