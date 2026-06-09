document.addEventListener("DOMContentLoaded", function () {
  var introLinks = document.querySelectorAll(
    '.bd-sidenav__home-link a.reference.internal[href$="intro.html"], .bd-sidenav__home-link a.reference.internal[href="./"]'
  );

  introLinks.forEach(function (link) {
    link.textContent = "240411100160";
  });
});
