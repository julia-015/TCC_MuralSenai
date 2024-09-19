const themeToggleBtn = document.getElementById('theme-toggle');
const body = document.body;

themeToggleBtn.addEventListener('click', () => {
    body.classList.toggle('dark-theme');

    // Atualiza o ícone com base no tema
    const icon = themeToggleBtn.querySelector('.material-symbols-outlined');
    if (body.classList.contains('dark-theme')) {
        icon.textContent = 'brightness_5'; // Ícone de "sol" para tema claro
    } else {
        icon.textContent = 'contrast'; // Ícone de "lua" para tema escuro
    }
});
