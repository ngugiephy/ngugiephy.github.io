$(window).on('load', function() {
  // Animate loader off screen
  // $("#splash_screen").delay(5000).fadeOut("slow");;
  // alert("adsf");
  $('#op').html('<div class="animate__animated animate__bounce" style="color:#00FF49;background-color: #616161;box-shadow: 0px 0px 8px #888888;padding:5px;margin-bottom:10px;margin-top:100px;">Content Loaded <i class="fa fa-check"></i></div><button type="button" class="btn btn-outline-success btn-lg" id="enter" style="box-shadow: 0px 0px 8px #888888;">Enter Scene</button>');

});

$( document ).ready(function() {
    $('#enter').click(function(){
      $("#splash_screen").fadeOut("slow");
      
      return false;
    });
});

$('#enter').click(function(){
      $("#splash_screen").fadeOut("slow");
      
      return false;
    });






const html = document.documentElement;
const canvas = document.getElementById("hero-lightpass");
const context = canvas.getContext("2d");

const frameCount = 125;
const currentFrame = index => (
  `img___/0001-050${index.toString().padStart(4, '000')}.jpg`
)

const preloadImages = () => {
  for (let i = 1; i < frameCount; i++) {
    const img = new Image();
    img.src = currentFrame(i);
  }
};

const img = new Image()
img.src = currentFrame(1);
canvas.width=1080;
canvas.height=1920;
img.onload=function(){
  context.drawImage(img, 0, 0);
}

const updateImage = index => {
  img.src = currentFrame(index);
  context.drawImage(img, 0, 0);
}

window.addEventListener('scroll', () => {  
  const scrollTop = html.scrollTop;
  const maxScrollTop = html.scrollHeight - window.innerHeight;
  const scrollFraction = scrollTop / maxScrollTop;
  const frameIndex = Math.min(
    frameCount - 1,
    Math.ceil(scrollFraction * frameCount)
  );
  
  requestAnimationFrame(() => updateImage(frameIndex + 1))
});

preloadImages()









// scroll indicator
window.addEventListener('scroll', function() {
   let totalHeight = document.body.scrollHeight -      window.innerHeight;
   let windowOffsetHeight = window.pageYOffset;
   let progress = document.querySelector('.progress');
   let percentage = (windowOffsetHeight * 100 / totalHeight)
    progress.style.width = percentage + "%";
});