from flask import Flask, request, render_template, jsonify
from importnb import Notebook
import requests, logging, os
from APIs.FluxoModf import pular_fluxo
from APIs.preencheForm import Camp_formsPre
from APIs.anexarArquivo import inserir_anexo
from APIs.anexarArquivo import inserir_anexo
app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return render_template("FrontHTML.html")

MAPA = {
     "AvancoFluxo": pular_fluxo,
     "altInfoCampo": Camp_formsPre,
     "anexarArquivo": inserir_anexo
}
@app.route("/executar", methods=["POST"])
@app.route("/executar", methods=["POST"])
def executar():

    # Se vier multipart (FormData)
    if request.content_type and "multipart/form-data" in request.content_type:
        data = request.form.to_dict()
    else:
        data = request.get_json(silent=True) or {}

    tipo = data.get("tipo")

    if tipo not in MAPA:
        return jsonify({"erro": "Ação inválida"}), 400

    # ---------------- AVANÇAR FLUXO ----------------
    if tipo == "AvancoFluxo":
        CdFluxo = data.get("CdFluxo")
        resultado = pular_fluxo(CdFluxo)

    # ---------------- ALTERAR CAMPO ----------------
    elif tipo == "altInfoCampo":
        CdFluxo = data.get("CdFluxo")
        CdTarefa = data.get("CdTarefa")
        CdCampo = data.get("CdCampo")
        Valor = data.get("Valor")
        resultado = Camp_formsPre(CdFluxo, CdTarefa, CdCampo, Valor)

    # ---------------- ANEXAR ARQUIVO ----------------
    elif tipo == "anexarArquivo":
        cdFluxo = data.get("cdFluxo")
        cdTarefa = data.get("cdTarefa")
        cdTipoAnexo = data.get("cd_Tipo_Anexo")
        dsAnexo = data.get("ds_Anexo")

        arquivo = request.files.get("dsNomeArquivoOriginal")

        if not arquivo:
            return jsonify({"erro": "Arquivo não enviado"}), 400

        os.makedirs("uploads", exist_ok=True)
        caminho = os.path.join("uploads", arquivo.filename)
        arquivo.save(caminho)

        resultado = inserir_anexo(cdFluxo, cdTarefa, cdTipoAnexo, dsAnexo, caminho)

    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)
