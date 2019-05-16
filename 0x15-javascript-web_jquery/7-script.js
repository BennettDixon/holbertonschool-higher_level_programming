const $ = window.$;
const url = 'https://swapi.co/api/people/5/?format=json;';

$.get(url, function (body) {
  let name = body['name'];
  $('#character').html(name);
});
