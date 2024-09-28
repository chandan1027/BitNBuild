var home = document.querySelector('#home');
var news=document.querySelector('#news');
var contact=document.querySelector('#contact');
var about=document.querySelector('#about')
var box = document.querySelector('.center-box');
function anima(){
    var t1 = gsap.timeline();

    t1.from(box, {
        duration: 0.5, 
        opacity: 0,
        x: -200,
        backgroundColor: '#ffffff'  // Add '#' for hex color
    },"auto")
    .to(box, {
        backgroundColor: '#ff0000'  // Add '#' for hex color
    },"auto");
}
home.addEventListener("click", () => {
    var t1 = gsap.timeline();

    t1.from(box, {
        duration: 0.5, 
        opacity: 0,
        x: -200,
        backgroundColor: '#ffffff'  // Add '#' for hex color
    },"auto")
    .to(box, {
        backgroundColor: '#ff0000'  // Add '#' for hex color
    },"auto");
});
news.addEventListener("click", () => {
    var t1 = gsap.timeline();

    t1.from(box, {
        duration: 0.5, 
        opacity: 0,
        x: -200,
        backgroundColor: '#ffffff'  // Add '#' for hex color
    },"auto")
    .to(box, {
        backgroundColor: '#000000'  // Add '#' for hex color
    },"auto");
});
contact.addEventListener("click", () => {
    var t1 = gsap.timeline();

    t1.from(box, {
        duration: 0.5, 
        opacity: 0,
        x: -200,
        backgroundColor: '#ffffff'  // Add '#' for hex color
    },"auto")
    .to(box, {
        backgroundColor: '#fff005'  // Add '#' for hex color
    },"auto");
});
about.addEventListener("click", () => {
    var t1 = gsap.timeline();

    t1.from(box, {
        duration: 0.5, 
        opacity: 0,
        x: -200,
        backgroundColor: '#ffffff'  // Add '#' for hex color
    },"auto")
    .to(box, {
        backgroundColor: '#ffffaa'  // Add '#' for hex color
    },"auto");
});
