#!/usr/bin/node
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (index, movie) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
