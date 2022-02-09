$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (results) {
    results.results.forEach(function (n) {
      $('#list_movies').append(`<li>${n.title}</li>`);
    });
  });
});
