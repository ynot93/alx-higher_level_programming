$(document).ready(function () {
  // Add a click event handler to the div with id "toggle_header"
  $('#toggle_header').click(function () {
    // Toggle the class "red" and "green" on the header
    $('header').toggleClass('red green');
  });
});
