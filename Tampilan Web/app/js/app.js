$(document).ready(function () {
  const $ = jQuery;
  $('nav.navbar').addClass('navbar-active');
  $(".navbar-nav .nav-link").hover(
    function () {
      $(this).css("color", "#007bff");
    },
    function () {
      $(this).css("color", "#333");
    }
  );

  $(".username-label").hover(
    function () {
      $(this).css("color", "#007bff");
    },
    function () {
      $(this).css("color", "#333");
    }
  );
});
function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}