const images = ["img1.jpg", "img2.jpg", "img3.jpg"];
let currentImage = 0;

function changeImage() {
  const img = document.getElementById("sliderImage");
  currentImage = (currentImage + 1) % images.length;
  img.src = images[currentImage];
}

setInterval(changeImage, 3000);

// Form validation
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("contactForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      const name = document.getElementById("name").value;
      const email = document.getElementById("email").value;
      const message = document.getElementById("message").value;

      if (!name || !email || !message) {
        alert("Please fill in all fields.");
        e.preventDefault();
      }
    });
  }
});