from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

aplikasi_paul = Flask(__name__)
aplikasi_paul.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
db = SQLAlchemy(aplikasi_paul)

# Membuat model untuk tabel 'users'
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

# Route untuk menampilkan semua data dari tabel 'users'
@aplikasi_paul.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

if __name__ == '__main__':
    aplikasi_paul.run()
