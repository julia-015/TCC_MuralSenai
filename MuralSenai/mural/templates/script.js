
document.addEventListener("DOMContentLoaded", () => {
    // URL da API para buscar a mensagem
    const apiUrl = "http://localhost:3000/api/aviso";

    // Referência ao elemento HTML onde a mensagem será exibida
    const noticeMessage = document.querySelector(".notice-message");

    // Busca a mensagem da API
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            // Atualiza o conteúdo com a mensagem vinda da API
            noticeMessage.textContent = data.mensagem || "Nenhuma mensagem disponível";
        })
        .catch(error => {
            console.error("Erro ao carregar o aviso:", error);
            noticeMessage.textContent = "Erro ao carregar a mensagem";
        });
});



document.addEventListener("DOMContentLoaded", () => {
    const apiUrl = "http://localhost:3000/api/aviso";
    const noticeMessage = document.querySelector(".notice-message");

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            noticeMessage.textContent = data.mensagem || "Nenhuma mensagem disponível";
        })
        .catch(error => {
            console.error("Erro ao carregar o aviso:", error);
            noticeMessage.textContent = "Erro ao carregar a mensagem";
        });
});
