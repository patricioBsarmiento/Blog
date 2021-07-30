from flaskblog import app
from OpenSSL import SSL

if __name__ == '__main__':
    app.run(debug=False)
