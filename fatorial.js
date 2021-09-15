function fatorial() {
    var numero = document.getElementById("numero"); // input do usuário
    var resultado = document.getElementById("resultado"); // output do sistema
    x = numero.value // corrige o input para poder ser trabalhado na função
    if (x < 0) {
        var controle = "Erro, não existe fatorial de números negativos";
    }
    else {
        if (x == 0) {
            var controle = 1;
        }
        else {
            var controle = 1;
            while (x >= 1) {
                controle *= x;
                x--;
            }
        }
    }
    resultado.innerHTML = controle; // comanda o retorno do output
}

