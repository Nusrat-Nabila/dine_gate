document.addEventListener("DOMContentLoaded", () => {
  // Profile Dropdown color change on click
  var dropdownToggle = document.querySelector('.profile-dropdown');

  if (dropdownToggle) {
    dropdownToggle.addEventListener('click', function() {
      this.classList.toggle('active'); // Toggle active class on click
    });
  }



