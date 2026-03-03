from flask import Flask, request, render_template, jsonify
from importnb import Notebook
import requests, logging, os
from APIs.FluxoModf import pular_fluxo
from APIs.preencheForm import Camp_formsPre
from APIs.anexarArquivo import inserir_anexo
from APIs.verifTarefa import Ver_Tarefa
#from waitress import serve

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return render_template("FrontHTML.html")


@app.route("/executar", methods=["POST"])
def executar():

    if request.content_type and "multipart/form-data" in request.content_type:
        data = request.form.to_dict()
    else:
        data = request.get_json(silent=True) or {}

    tipo = data.get("tipo")

    # ---------------- AVANÇAR FLUXO ----------------
    if tipo == "AvancoFluxo":
        CdFluxo = data.get("CdFluxo")
        resultado = pular_fluxo(CdFluxo)

    # ---------------- ALTERAR CAMPO ----------------
    elif tipo == "altInfoCampo":
        CdFluxo = data.get("CdFluxo")
        CdCampo = data.get("CdCampo")
        Valor = data.get("Valor")
        resultado = Camp_formsPre(CdFluxo, CdCampo, Valor)

    # ---------------- ANEXAR ARQUIVO ----------------
    elif tipo == "anexarArquivo":
        cdFluxo = data.get("cdFluxo")
        dsAnexo = data.get("ds_Anexo")
        arquivo = request.files.get("dsNomeArquivoOriginal")

        if not arquivo:
            return jsonify({"erro": "Arquivo não enviado"}), 400

        os.makedirs("uploads", exist_ok=True)
        caminho = os.path.join("uploads", arquivo.filename)
        arquivo.save(caminho)

        resultado = inserir_anexo(cdFluxo, dsAnexo, caminho)
    # --------------- Verificar Tarefa --------------
    
    elif tipo == "verifTarefa":
        cdProcesso = data.get("cdProcesso")
        cdFluxo = data.get("cdFluxo")
        resultado = Ver_Tarefa(cdProcesso, cdFluxo, token)


    return jsonify(resultado)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000, threads=8)
