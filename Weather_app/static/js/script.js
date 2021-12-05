const hamburger = document.querySelector('.hamburger')
const navmenu = document.querySelector('.nav-menu')
const navbar = document.querySelector('.navbar')
const navLink = document.querySelectorAll('.nav-link')

hamburger.addEventListener('click',menubar)
function menubar(){
   hamburger.classList.toggle("active")
   navmenu.classList.toggle("active")
   navbar.classList.toggle("active")
}

navLink.forEach(n => n.addEventListener("click",closeMenu))
function closeMenu(){
  hamburger.classList.remove('active');
  navmenu.classList.remove('active');
}
