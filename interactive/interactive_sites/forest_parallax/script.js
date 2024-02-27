let text = document.getElementById('text')
let bird1 = document.getElementById('bird1')
let bird2 = document.getElementById('bird2')
let btn = document.getElementById('btn')
let rocks = document.getElementById('rocks')
let forest = document.getElementById('forest')
let water = document.getElementById('water')


window.addEventListener('scroll', function(){
	let value = window.scrollY

	text.style.top = 100 +  value * -0.5 + '%'
	bird1.style.top =  value * -0.5 + '%'
	bird2.style.top =  value * -0.5 + '%'
	btn.style.top =  value * 0.1 + '%'
	rocks.style.top =  value * 0.4 + '%'
	forest.style.top =  value * 0.5 + '%'
	water.style.top =  value * 0.3 + '%'
})