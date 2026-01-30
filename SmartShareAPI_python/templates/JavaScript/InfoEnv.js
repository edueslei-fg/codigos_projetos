function enviar(){
            fetch("/dados", {

                method: "POST",
                headers: {"Content-Type": "application/json"},
                body:JSON.stringify({nome:document.getElementById("nome").value})
            },
            
        )
        .then(r => r.text())
        .then(resp => alert(resp));
    }