
function Video(id) {
    document.querySelectorAll("video").forEach(video => {
        video.pause();
        video.style.display = "none";
    });

    const video = document.getElementById(id);
    video.style.display = "block";
    video.play();
    const source = video.querySelector("source").src;
    setTimeout(() => location.reload(), 100);
    window.open(source, "_blank");
}
