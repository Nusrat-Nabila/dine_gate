document.addEventListener("DOMContentLoaded", () => {
  const logo = document.getElementById("dinegate-logo");

  if (logo) {
    logo.addEventListener("mouseenter", () => {
      logo.style.opacity = "0.85";
    });

    logo.addEventListener("mouseleave", () => {
      logo.style.opacity = "1";
    });
  }
});
