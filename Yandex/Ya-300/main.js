'use strict'

window.onload = function () {
  app()
}

function app() {
  var items = document.querySelectorAll('.choise-item'),
      lastwindow = document.querySelector('.screen');

  items.forEach((element) => {
    element.addEventListener('click', () => {
      lastwindow.classList.add('open')
    })
  });


}
