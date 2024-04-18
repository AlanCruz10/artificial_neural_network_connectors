const video = document.getElementById('video-feed');
let stream;
const constraints = {
    video: {
        width: { ideal: 640 },
        height: { ideal: 640 }
    }
};

navigator.mediaDevices.getUserMedia(constraints)
    .then(mediaStream => {
        video.srcObject = mediaStream;
        stream = mediaStream;
    })
    .catch(error => {
        console.error('Error accessing webcam:', error);
    });
// Función para capturar un fotograma y enviarlo al backend
function captureFrame() {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append('file', blob, 'photo.jpg');

        fetch('/', {
            method: 'POST',
            body: formData,
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => console.log(response.text()))
        .then(result => {
            console.log(result)
            const resultContainer = document.getElementById('result-container');
            resultContainer.innerHTML = result
        })
        .catch(error => {
            console.error('Error uploading image:', error);
        });
    }, 'image/jpeg');
}

// Evento click para capturar un fotograma cuando se presiona el botón
document.getElementById('capture-btn').addEventListener('click', captureFrame);