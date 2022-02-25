/*
//Not sure if I will use this yet

var itemsbyviewport;
var mq = window.matchMedia( "(min-width: 321px)" );
if (mq.matches) {
    itemsbyviewport = 2; //width less than 376 in this case
}
else {
     itemsbyviewport = 5; // width greater than 376 in this case
}
*/


/* From Tiny slider https://github.com/ganlanyuan/tiny-slider */
tns({
    container: '.slider',
    mode: 'carousel', // or 'gallery'
    axis: 'horizontal', // or 'vertical'
    items: 5,
    gutter: 0,
    edgePadding: 0,
    fixedWidth: false,
    slideBy: 1,
    controls: false,
    controlsText: ['prev', 'next'],
    controlsContainer: false,
    nav: false,
    navContainer: false,
    navAsThumbnails: false,
    arrowKeys: false,
    speed: 300,
    autoplay: true,
    autoplayTimeout: 3000,
    autoplayDirection: 'forward',
    autoplayText: ['start', 'stop'],
    autoplayHoverPause: false,
    autoplayButton: false,
    autoplayButtonOutput: false,
    autoplayResetOnVisibility: true,
    loop: true,
    rewind: false,
    autoHeight: false,
    responsive: false,
    lazyload: true,
    touch: true,
    mouseDrag: false,
    swipeAngle: 15,
    nested: false,
    freezable: true,
    onInit: false
  });