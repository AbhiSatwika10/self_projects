document.addEventListener("DOMContentLoaded", () => {

    const btn = document.getElementById("verifyBtn");
    const result = document.getElementById("result");

    if(btn){
        btn.addEventListener("click", () => {
            result.innerText =
            "✅ Enterprise AI Auto-Scan Running.\nOpen any website to see live analysis.";
        });
    }

});