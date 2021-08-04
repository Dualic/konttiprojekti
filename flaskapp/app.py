
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from datetime import datetime
import psycopg2
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db




def get_db_connection():
    
    conn = psycopg2.connect(**config())
    
    return conn
    

def get_post(cursor, post_id):
    conn = get_db_connection()
    cursor = conn.cursor()  
    SQL = 'SELECT * FROM posts WHERE id = %s;'
    cursor.execute(SQL, (post_id,))
    post = cursor.fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post




app = Flask(__name__)


app.config['SECRET_KEY'] = 'do_not_touch_or_you_will_be_fired'


# this function is used to format date to a finnish time format from database format
# e.g. 2021-07-20 10:36:36 is formateed to 20.07.2021 klo 10:36
def format_date(post_date):
    isodate = post_date.replace(' ', 'T')
    newdate = datetime.fromisoformat(isodate)
    return newdate.strftime('%d.%m.%Y') + ' klo ' + newdate.strftime('%H:%M')


# this index() gets executed on the front page where all the posts are
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()  
    cursor.execute('SELECT * FROM posts;')
    posts = cursor.fetchall()
    conn.close()
    # we need to iterate over all posts and format their date accordingly
    dictrows = [dict(row) for row in posts]
    for post in dictrows:
        # using our custom format_date(...)
        post['created'] = format_date(post['created'])
    return render_template('index.html', posts=dictrows)


# here we get a single post and return it to the browser
@app.route('/<int:post_id>')
def post(post_id):
    post = dict(get_post(post_id))
    post['created'] = format_date(post['created'])
    return render_template('post.html', post=post)


# here we create a new post
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            cursor = conn.cursor() 
            cursor.execute('INSERT INTO posts (title, content) VALUES (%s, %s);',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            cursor = conn.cursor() 
            cursor.execute('UPDATE posts SET title = %s, content = %s WHERE id = %s;',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


# Here we delete a SINGLE post.
@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)

    conn = get_db_connection()
    cursor = conn.cursor() 
    cursor.execute('DELETE FROM posts WHERE id = %s;', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))
