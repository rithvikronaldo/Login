var myIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}    
  x[myIndex-1].style.display = "block";  
  setTimeout(carousel, 2000); // Change image every 2 seconds
}

/*SCROLL TO NEW NAVBAR*/
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 655 || document.documentElement.scrollTop > 655) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-50px";
  }
}

/*CHANGE BG COLOR ON SCROLL*/
var body = document.getElementsByTagName('body')[0];
        body.style.backgroundColor = 'white';

        // trigger this function every time the user scrolls
        window.onscroll = function (event) {
            var scroll = window.pageYOffset;
            if (scroll < 2200) {
                // green
                body.style.backgroundColor = 'white';
            } else if (scroll >= 2200 && scroll < 3400) {
                // yellow
                body.style.backgroundColor = 'black';
            }
            else{
                body.style.backgroundColor = 'white';
            }
        }

/*ON SCROLL fixed and scrollable*/
