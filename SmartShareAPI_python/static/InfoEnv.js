const camposPorTipo = {
  AvancoFluxo: `
            <label for="Código do Fluxo">Código do Fluxo</label>
            <input type="number" id="CdFluxo" placeholder="Código do Fluxo">
          `,
  altInfoCampo: `
            <label for="Código do Fluxo">Código do Fluxo</label>
            <br>
            <input type="number" class="InputInfo" id="CdFluxo" placeholder="Código do Fluxo">
            <br>
            <label for="Código do Fluxo">Campo para alteração</label>
            <br>
            <input type="text" class="InputInfo" id="CdCampo" placeholder="Código do Campo para alteração">
            <br>
            <label for="Código do Fluxo">Valor</label>
            <br>
            <input type="text" class="InputInfo" id="Valor" placeholder="Valor">
  `,
  anexarArquivo:`
            <label for="Código do Fluxo">Código do Fluxo</label>
            <br>
            <input type="text" class="InputInfo" id="cdFluxo" placeholder="cdFluxo">
            <br>
            <label for="Descrição do Anexo">Descrição do Anexo</label>
            <br>
            <input type="text" class="InputInfo" id="ds_Anexo" placeholder="dsAnexo">
            <br>
            <label for="Nome do Arquivo">Nome do Arquivo</label>
            <br>
            <input type="file" class="InputInfo" id="dsNomeArquivoOriginal" placeholder="dsNomeArquivoOriginal">
  `,
  verifTarefa:`
            <label for="Código do Processo">Código do Processo</label>
            <br>
            <input type="text" class="InputInfo" id="cdProcesso" placeholder="cdProcesso">
            <br>
  `
}
document.getElementById("tipo").addEventListener("change", e => {
  document.getElementById("campos").innerHTML =
    camposPorTipo[e.target.value] || ""
})


function enviar(){

  const tipo = document.getElementById("tipo").value
  const inputs = document.querySelectorAll("#campos input")

  let formData = new FormData()
  formData.append("tipo", tipo)

  inputs.forEach(i => {
    if (i.type === "file") {
      if (i.files.length > 0) {
        formData.append(i.id, i.files[0])
      }
    } else {
      formData.append(i.id, i.value)
    }
  })

  fetch("/executar", {
    method: "POST",
    body: formData
  })
  .then(r => r.json())
  .then(resp => alert(resp.body?.message || JSON.stringify(resp.body)))
}

