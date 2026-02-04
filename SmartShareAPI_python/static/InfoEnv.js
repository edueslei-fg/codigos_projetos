function enviar(){
            fetch("/dados", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body:JSON.stringify({CdFluxo:document.getElementById("CdFluxo").value})
            },
            
        )
        .then(r => r.text())
        .then(response => alert(response));
    }