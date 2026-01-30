from flask import Flask, request, render_template
from serviço import processar_nome

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("FrontHTML.html")

@app.route("/dados", methods=["POST"])
def dados():
    data = request.json
    CdFluxo = data["CdFluxo"]
    CdTarefa = data["CdTarefa"]
    

    resultado = processar_nome(CdFluxo,CdTarefa)

    return resultado

if __name__ == "__main__":
    app.run(debug=True)
