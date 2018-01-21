'use strict'

function changeColor(e) {
  var color = '#cc0000';
  e.target.style.backgroundcolor = color;
}

var divs = document.querySelectorAll('.d-md-flex');
divs.forEach(function(div){
  div.addEventListener('click', changeColor);
});
