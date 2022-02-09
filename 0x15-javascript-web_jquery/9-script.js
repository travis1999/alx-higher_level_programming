$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (result) {
    $('#hello').text(result.hello);
  });
});
