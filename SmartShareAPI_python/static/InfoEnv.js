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
            <label for="Código do Fluxo">Código da Tarefa</label>
            <br>
            <input type="number" class="InputInfo" id="CdTarefa" placeholder="Código da Tarefa">
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
            <label for="Código da Tarefa">Código da Tarefa</label>
            <br>
            <input type="text" class="InputInfo" id="cdTarefa" placeholder="cdTarefa">
            <br>
            <label for=">Código do Tipo no Anexo">Código do Tipo no Anexo</label>
            <br>
            <input type="text" class="InputInfo" id="cd_Tipo_Anexo" placeholder="cdTipoAnexo">
            <br>
            <label for="Descrição do Anexo">Descrição do Anexo</label>
            <br>
            <input type="text" class="InputInfo" id="ds_Anexo" placeholder="dsAnexo">
            <br>
            <label for="Nome do Arquivo">Nome do Arquivo</label>
            <br>
            <input type="file" class="InputInfo" id="file_path" placeholder="dsNomeArquivoOriginal">
  `
}
document.getElementById("tipo").addEventListener("change", e => {
  document.getElementById("campos").innerHTML =
    camposPorTipo[e.target.value] || ""
})


function enviar(){
  const tipo = document.getElementById("tipo").value
  const inputs = document.querySelectorAll("#campos input")

  // 👉 se for upload, usa FormData
  if (tipo === "anexarFluxo") {
    let formData = new FormData()
    formData.append("tipo", tipo)

    inputs.forEach(i => {
      if (i.type === "file") {
        formData.append("arquivo", i.files[0])
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

    return
  }

  // 👉 outros tipos continuam JSON
  let data = { tipo }
  inputs.forEach(i => data[i.id] = i.value)

  fetch("/executar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
  .then(r => r.json())
  .then(resp => alert(resp.body?.message || JSON.stringify(resp.body)))
}

