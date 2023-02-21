// Updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header.

const $ = window.$;

// Modify CSS of header
$('#red_header').on('click', function () {
  $(this).css('color', '#FF0000');
});
