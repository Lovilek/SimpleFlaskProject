from flask import Flask, render_template, request
import requests

app = Flask(__name__)

blogs = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()

print(blogs)


@app.route('/')
def get_all_posts():
    return render_template("index2.html", all_posts=blogs)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        return f"f<h1>{name} {email} {phone} {message}</h1>"

    return render_template("contact.html")


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in blogs:
        if post["id"] == index:
            requested_post = post

    return render_template("post2.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=False)
