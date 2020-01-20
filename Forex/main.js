'use strict'

window.onload = function () {
  app()
}

function app() {
  var items = document.querySelectorAll('.choise-item'),
      buttons = document.querySelectorAll('.modal__button'),
      peoples = document.querySelectorAll('.people__item'),
      tool = document.querySelector('.modal_tool'),
      trade = document.querySelector('.modal_trade'),
      title = document.querySelector('.title'),
      lastwindow = document.querySelector('.screen'),
      index = 0;

      console.log(peoples[1]);

  items.forEach((element) => {
    element.addEventListener('click', () => {
      var thisEl = event.target;
      thisEl.classList.add('open')
      title.classList.remove('open')
      items[0].classList.add('disabled')
      items[1].classList.add('disabled')
      setTimeout(() => {
        if (thisEl.classList.contains('choise-item_tool')) {
          tool.classList.add('open')
        }else{
          trade.classList.add('open')
        }
      }, 1000)
    })
  });

  buttons.forEach((element) => {
    element.addEventListener('click', () => {
      event.target.parentElement.parentElement.classList.remove('open');
      items[0].classList.remove('disabled')
      items[1].classList.remove('disabled')
      index++
      if (index === 2) {
        lastwindow.classList.add('open')
      }else{
        title.classList.add('open')
      }
      if (index === 1) {
        peoples[1].classList.add('open')
        peoples[0].classList.remove('open')
      }
    })
  });


}
