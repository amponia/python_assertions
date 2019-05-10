#creating user interface
#bringing blog and post together
#show the user the available blogs
    # let the user make a choice
    # do something with that choice
    # eventually exit

menu_prompt: str = 'Enter C to create blog, L to list blogs, R to read one, P to create a post, Q to quit'
POST_TEMPLATE = '''---{}--- {}'''

from blog import Blog
from post import Post

blogs = dict ()

def menu():

    print_blogs ()
    selection = input(menu_prompt)
    while selection != 'Q':
        if selection == 'C':
            ask_create_blog ()
        elif selection == 'R':
            ask_read_blog ()
        elif selection == 'P':
            ask_create_post()
        selection = 'Q'

def print_blogs(): #print the available blogs. aby to zrobic, trzeba zrobic iteracje po slowniku
    for key, blog in blogs.items(): # podaje listę keys i values:[(blog_name, Blog), (blog_name, Blog)]
        print ('-{}'.format(blog))


def ask_create_blog() :
    title = input ('Enter your blog title: ') #1st side effect
    author = input('Enter your name: ') # 2nd side effect

    blogs[title] = Blog (title, author) # dictionary "blogs" and the key "title". If the key doesn't exist, it is created.


def ask_read_blog():
    title = input ('enter the blog title you want to read: ')

    print_posts (blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post (post):
    print (POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    blog_name = input("enter blog title")
    title = input("enter post title")
    content = input ("enter post content")

    blogs[blog_name].create_post(title, content)