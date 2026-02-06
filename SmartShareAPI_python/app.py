from flask import Flask, request, render_template, jsonify
from APIs.FluxoModf import pular_fluxo
from APIs.preencheForm import Camp_formsPre
from APIs.anexarArquivo import inserir_anexo

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
    
    elif tipo == "AvancoFluxo":
        CdFluxo = data.get("CdFluxo")
        resultado = pular_fluxo(CdFluxo)

    elif tipo == "altInfoCampo":
        CdFluxo = data.get("CdFluxo")
        CdTarefa = data.get("CdTarefa")
        CdCampo = data.get("CdCampo")
        Valor = data.get("Valor")
        resultado = Camp_formsPre(CdFluxo, CdTarefa, CdCampo, Valor)

    elif tipo == "anexarFluxo":
        CdFluxo = data.get("CdFluxo")
        CdTarefa = data.get("CdTarefa")
        cdTipoAnexo = data.get("cdTipoAnexo")
        dsAnexo = data.get("dsAnexo")
        dsNomeArquivoOriginal = data.get("dsNomeArquivoOriginal")
        resultado = inserir_anexo()
        

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)
