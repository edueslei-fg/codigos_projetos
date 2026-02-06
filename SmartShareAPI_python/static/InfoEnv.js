const camposPorTipo = {
  AvancoFluxo: `
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
  anexarFluxo:`
            <label for="Código do Fluxo">Valor</label>
            <br>
            <input type="text" class="InputInfo" id="Valor" placeholder="Valor">
  `
}
document.getElementById("tipo").addEventListener("change", e => {
document.getElementById("campos").innerHTML = camposPorTipo[e.target.value] || ""
})

if (tipo = "anexarFluxo"){
  let formData = new FormData()
  formData.append("tipo", tipo)
  formData.append("arquivo", fileInput.files[0])
}
function enviar(){
  const tipo = document.getElementById("tipo").value
  const inputs = document.querySelectorAll("#campos input")
  let data = { tipo }

  inputs.forEach(i => data[i.id] = i.value)
  
  fetch("/executar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
.then(r => r.json())
.then(resp => {alert(resp.body?.message || JSON.stringify(resp.body));
})
}



