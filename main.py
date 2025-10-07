from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>Currículo</title></head>
        <body>
            <h1>Luiza Petenazzi</h1>
            <p>Email: luiza.petenazzi@sou.inteli.edu.br</p>
            <p>Aluna do segundo ano de engenharia da computação no Inteli.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
