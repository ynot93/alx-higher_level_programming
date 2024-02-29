$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data) {
    data.results.forEach(function (movie) {
      const title = movie.title;

      const listItem = $('<li>').text(title);

      $('#list_movies').append(listItem);
    });
  });
});
