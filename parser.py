from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "<h2>welcome to the homepage<h2>"



if __name__ == '__main__':
    app.run(debug=True)

