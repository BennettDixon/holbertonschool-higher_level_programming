const $ = window.$;
const url = "https://fourtonfish.com/hellosalut/?lang=fr";

$.get(url, function(body) {
  let hello = body["hello"];
  $("#hello").html(hello);
});
