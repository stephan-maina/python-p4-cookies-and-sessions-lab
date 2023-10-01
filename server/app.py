from flask import Flask, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import BlogPost

@app.route('/articles/<int:id>')
def view_article(id):
    # Initialize 'page_views' in the session if it doesn't exist
    session['page_views'] = session.get('page_views', 0)

    # Increment 'page_views' for each request
    session['page_views'] += 1

    # Check if the user has viewed more than 3 pages
    if session['page_views'] > 3:
        return jsonify({'message': 'Maximum pageview limit reached'}), 401

    # Retrieve the requested article by ID
    article = BlogPost.query.get(id)

    if article is None:
        return jsonify({'message': 'Article not found'}), 404

    return jsonify({'title': article.title, 'content': article.content})

@app.route('/clear')
def clear_session():
    # Clear the session and reset 'page_views'
    session.clear()
    return jsonify({'message': 'Session cleared'})

if __name__ == '__main__':
    app.run(debug=True)
