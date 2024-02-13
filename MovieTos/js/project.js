// responsive navbar
let a = 0 ;
var navBar = document.getElementById('navBar');
function navFunction(){
  a++;
  if(a%2===0){
    navBar.style.right = '-100%';
  }
  else{
    navBar.style.right = 0
  }
}


// hover effect for add to watchlist
var bookMark = document.querySelectorAll
(".bookmark");
for (var i = 0; i < bookMark.length; i++) {
    bookMark[i].addEventListener("mouseover", opacityYes);
    bookMark[i].addEventListener("mouseout", opacityNo);
  }

function opacityYes(){
    this.nextElementSibling.style.opacity = 1;
}

function opacityNo(){
    this.nextElementSibling.style.opacity = 0;
}


// Thumbnail image controls
let slideIndex = 0;
showSlides();

function showSlides(){
  let i;
  let slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, 5000);
}
// FAQ section
const faqFunc = (qtn) => {
  const ansBox = qtn.nextElementSibling; // Get the next sibling, which is the answer box
  const icon = qtn.querySelector('.bx');

  ansBox.classList.toggle('show');
  icon.classList.toggle('bx-chevron-up');
  icon.classList.toggle('bx-chevron-down');
};





