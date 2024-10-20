from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Bem-vindo(a) à API hospedada no GitHub!")

if __name__ == '__main__':
    app.run(debug=True)
