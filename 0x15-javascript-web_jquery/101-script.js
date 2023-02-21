// adds, removes and clears LI elements from a list when the user clicks.

const $ = window.$;

$(document).ready(function () {
  // When add_item div is clicked
  $('DIV#add_item').on('click', function () {
    // Add a new list item
    $('UL.my_list').append('<li>Item</li>');
  });

  // When remove_item div is clicked
  $('DIV#remove_item').on('click', function () {
    // Remove last list item
    $('UL.my_list li').last().remove();
  });

  // When clear_list is clicked
  $('DIV#clear_list').on('click', function () {
    // Remove all elements in the list
    $('UL.my_list li').remove();
  });
});
