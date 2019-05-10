from post import Post

class Blog:
    def __init__(self):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return "Blog Title by Blog Author (0 posts)"
        return '{} by {} ({} post{})'.format(
            self.title,
            self.author,
            len(self.posts),
            's' if len(self.posts) != 1
            else '')

    def create_post (self, title, content):
        self.posts.append(Post(title,content))

    def json (self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }



