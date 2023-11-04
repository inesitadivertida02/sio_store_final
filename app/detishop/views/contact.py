from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'seu_usuario_mysql'
app.config['MYSQL_PASSWORD'] = 'sua_senha_mysql'
app.config['MYSQL_DB'] = 'mydatabase'  # Nome do banco de dados criado

# Criação da conexão MySQL
mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

# Rota principal
@app.route('/')
def index():
    cursor = mysql.cursor(dictionary=True)
    cursor.execute("SELECT * FROM feedback")
    data = cursor.fetchall()
    cursor.close()
    return render_template('contact.html')

# Rota para inserir feedback
@app.route('/feedback', methods=['POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        cursor = mysql.cursor()
        cursor.execute("INSERT INTO feedback (name, email, subject, message) VALUES (%s, %s, %s, %s)",
                       (name, email, subject, message))
        mysql.commit()
        cursor.close()

    return redirect('/')

@app.route('/ver_feedback')
def ver_feedback():
    cursor = mysql.cursor(dictionary=True)
    cursor.execute("SELECT * FROM feedback")
    data = cursor.fetchall()
    cursor.close()
    return render_template('ver_feedback.html', feedback=data)


if __name__ == '__main__':
    app.run(debug=True)
