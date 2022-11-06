from flask import Flask
app = Flask(MVC)
@app.route('/')
def example_page():
    db = get_db()
    query = db.execute('select * from entries order by id desc')
    entries = query.fetchall()
    return render_template('example_page.html', entries=entries)

if __name__ == '__main__':
    app.run

