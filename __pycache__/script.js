const video = document.getElementById('video');

navigator.mediaDevices.getUserMedia({
    video: {
        width: 640,
        height: 480,
        facingMode: "user"
    }
})
.then(stream => {
    video.srcObject = stream;
});

async function capture(){

    const result = document.getElementById("result");
    result.innerText = "Analyzing with AI...";

    const canvas = document.createElement('canvas');

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext('2d');
    ctx.drawImage(video,0,0,canvas.width,canvas.height);

    canvas.toBlob(async blob => {

        try{

            let formData = new FormData();
            formData.append("file", blob, "frame.jpg");

            const res = await fetch("http://127.0.0.1:8000/verify",{
                method:"POST",
                body:formData
            });

            const data = await res.json();

            let text =
                "Status: "+data.status+
                " | Risk: "+data.risk+
                " | Blink: "+data.blink+
                " | FaceMatch: "+data.face_match;

            result.innerText = text;

            if(data.risk === "LOW"){
                result.style.color = "lightgreen";
            }else{
                result.style.color = "red";
            }

        }catch(err){
            result.innerText = "Backend not responding!";
            result.style.color = "orange";
            console.log(err);
        }

    }, "image/jpeg", 0.7); // 🔥 faster compression
}