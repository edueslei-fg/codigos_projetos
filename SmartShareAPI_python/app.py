from flask import Flask, request, render_template
from APIs.FluxoModf import pular_fluxo

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("FrontHTML.html")

@app.route("/dadosAnvanco", methods=["POST"])
def dadosAnvanco():
    data = request.json

    CdFluxo = int(data["CdFluxo"])  # converte pra número

    print("Código", CdFluxo, "recebido")

    resultado = pular_fluxo(CdFluxo)

    return resultado

if __name__ == "__main__":
    app.run(debug=True)
