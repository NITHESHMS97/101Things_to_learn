from flask import Blueprint, render_template, request, flash, redirect, url_for
from api import db
from .blog_models import Post
blog = Blueprint("blog",__name__)

@blog.route("/")
@blog.route("/home")
def home():
    posts = Post.query.all()
    print(posts)
    serialized_data = []
    for post in posts:
        serialized_data.append(post.serialize)
    print(serialized_data)
    return render_template('home.html',data=serialized_data)

@blog.get("/post/<string:title>")
def display_post(title):
    posttoDispaly = Post.query.filter_by(title = title).first()
    print(posttoDispaly)
    return render_template('post.html',post=posttoDispaly)

@blog.route("/create",methods=['GET','POST'])
def createBlog():
    if request.method == 'POST':
        title =  request.form.get('title')
        content = request.form.get('description')
        title_exist = Post.query.filter_by(content=title).first()
        if not title:
            flash('Title missing')
        elif title_exist:
            flash('Title already exists!')
        else:
            new_post = Post(title=title,content=content)
            print(content)
            db.session.add(new_post)
            db.session.commit()
            flash('Post created')
            print('Post created')
            return redirect(url_for('blog.home'))


    return render_template('create_post.html')