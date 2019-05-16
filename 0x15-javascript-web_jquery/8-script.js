const $ = window.$;
const url = "https://swapi.co/api/films/?format=json";

$.get(url, function(body) {
  let films = body["results"];
  let list = $("#list_movies");
  films.forEach(element => {
    list.append("<li>" + element["title"] + "</li>\n");
  });
});
