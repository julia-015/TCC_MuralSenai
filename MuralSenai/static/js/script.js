document.addEventListener("DOMContentLoaded", function(){
    const themeToogleBtn = document.getElementById("theme-toogle");
    let currentTheme = localStorage.getItems("theme") || "light";
    document.documentElement.setAttribute("data-theme", currentTheme);

    themeToogleBtn.addEventListener("click", function(){
        currentTheme = currentTheme === "light" ? "dark" : "light";
        document.documentElement.setAttribute("data-theme", currentTheme);
        localStorage.setItem("theme", currentTheme);
    });
});