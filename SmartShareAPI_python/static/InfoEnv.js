function enviarAvanco(){
            fetch("/dadosAnvanco", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body:JSON.stringify({CdFluxo:document.getElementById("CdFluxo").value})
            },
            
        )
        .then(r => r.text())
        .then(response => alert(response));
    }
    function enviarAlteracao(){
        fetch("/enviarAlteracao",{
            method:"POST",
            headers:{"Cotent-Type":"application/json"},
            body: JSON.stringify({
                CdFluxo:document.getElementById("CdFluxo").value, 
                CdTarefa:document.getElementById("CdTarefa").value, 
                CdCampo:document.getElementById("CdCampo").value,
                Valor:document.getElementById("Valor").value 
            })
        })
    }