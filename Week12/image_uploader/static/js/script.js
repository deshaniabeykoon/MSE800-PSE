// Toggle between two static images
function toggleImage() {
    const imgElement = document.getElementById('loadedImage');
    if (imgElement.src.includes("example.jpg")) {
        imgElement.src = "/static/images/another_example.jpg";
    } else {
        imgElement.src = "/static/images/example.jpg";
    }
}

// Dynamically change image to uploaded one
function changeToUploadedImage(newSrc) {
    document.getElementById("loadedImage").src = newSrc;
}
