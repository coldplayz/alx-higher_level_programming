// fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

const $ = window.$;

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (responseData, textStatus) {
  for (const obj of responseData.results) {
    $('#list_movies').append(`<li>${obj.title}</li>`);
  }
});
