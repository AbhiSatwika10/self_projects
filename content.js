(function(){

    console.log("AI Reality Check scanning page...");

    let pageText = document.body.innerText;

    // ⭐ Fake AI scoring logic (replace later with backend)
    let suspiciousWords = ["shocking","breaking","secret","100%","guaranteed","click here"];
    let risk = 0;

    suspiciousWords.forEach(word=>{
        if(pageText.toLowerCase().includes(word)){
            risk += 10;
        }
    });

    let trustScore = Math.max(20, 100 - risk);

    showOverlay(trustScore);

})();

function showOverlay(score){

    let box = document.createElement("div");

    box.style.position="fixed";
    box.style.bottom="20px";
    box.style.right="20px";
    box.style.background="#111";
    box.style.color="white";
    box.style.padding="15px";
    box.style.zIndex="999999";
    box.style.borderRadius="10px";
    box.style.fontSize="14px";
    box.innerHTML = "🤖 AI Trust Score: <b>"+score+"%</b>";

    document.body.appendChild(box);
}