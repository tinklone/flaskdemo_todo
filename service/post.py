from model.models import db
from model.models import Post,Category
class PostService():
    def __init__(self):
        pass
    def save(self,content,category_name):
        category = Category(category_name)
        post = Post(content,content,category)
        db.session.add(post)
        db.session.commit()
    def get_list(self):
        post_list = Post.query.all()
        return post_list