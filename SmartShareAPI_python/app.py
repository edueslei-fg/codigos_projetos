from flask import Flask, request, render_template, jsonify
from APIs.FluxoModf import pular_fluxo
from APIs.preencheForm import Camp_formsPre

app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    return render_template("FrontHTML.html")

MAPA = {
     "AvancoFluxo": pular_fluxo,
     "altInfoCampo": Camp_formsPre
}
@app.route("/executar", methods=["POST"])
def executar():
    data = request.json
    tipo = data.get("tipo")

    if tipo not in MAPA:
        return jsonify({"erro": "Ação inválida"}), 400

    resultado = MAPA[tipo](data)

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)
