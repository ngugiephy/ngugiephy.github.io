var frameNumber = 0,

playbackConst = 1000,

setHeight = document.getElementById("set-height")

vid = document.getElementById('v1');


vid.addEventListener('loadedmetadata', function(){
	setHeight.style.height = Math.floor(vid.duration) * playbackConst + "px";
});

function scrollPlay(){
	var frameNumber = window.pageYOffset/playbackConst;
	vid.currentTime = frameNumber;
	window.requestAnimationFrame(scrollPlay);
}
window.requestAnimationFrame(scrollPlay);