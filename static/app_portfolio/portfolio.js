const nav = document.getElementsByClassName('navbar');
window.onscroll = function () { 
    if (document.body.scrollTop >= 200 ) {
        nav.classList.add("navbar-toggled");
        nav.classList.remove("navbar");
    } 
    else {
        nav.classList.add("navbar");
        nav.classList.remove("navbar-toggled");
    }
};