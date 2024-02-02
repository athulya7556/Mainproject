document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('#animation-container img');
    let currentIndex = 0;

    function showNextImage() {
      images[currentIndex].classList.remove('visible');
      currentIndex = (currentIndex + 1) % images.length;
      images[currentIndex].classList.add('visible');
    }

    setInterval(showNextImage, 2000); // Change the interval time (in milliseconds) as needed
  });


  document.querySelector("#siteLayout > div > div:nth-child(13) > div")

