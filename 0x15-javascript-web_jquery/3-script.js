// Adds the class red to the <header> element when the user clicks on the tag DIV#red_header.

const $ = window.$;

// Modify CSS of header
$('#red_header').on('click', function () {
  $('header').attr('class', 'red');
});
