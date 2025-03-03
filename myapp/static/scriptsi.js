
const content = document.querySelector('.content')
const modal = document.querySelector('.modal')
const toggle = document.querySelector('.toggle')
let isActive = false

toggle.onclick = function(){
  if (isActive) {
    content.classList.remove('active')
    modal.classList.remove('active')
    isActive = false
  } else {
    content.classList.add('active')
    modal.classList.add('active')
    isActive = true
  }
}



