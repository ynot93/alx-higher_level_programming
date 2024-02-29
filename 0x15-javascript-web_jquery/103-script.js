$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();

    const url = 'https://www.fourtonfish.com/hellosalut/hello/';
    $.get(url, { lang: languageCode }, function (data) {
      const helloTranslation = data.hello;

      $('#hello').text(helloTranslation);
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
