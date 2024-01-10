#!/usr/bin/node
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (names) {
      $('DIV#character').append(names.name);
    }
  });
});
