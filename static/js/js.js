$(function() {
  /*bootsrap popover for chart*/
  $('[data-toggle="popover"]').popover()
  $("#hide").click(function() {
    $(".1").toggle();
  });
  /*hides holiday on the rota and chat*/
  array = []
  $('.hide').toggle(function() {
    $(".test").each(function() {
      array.push(
        $(this).text());


    });
    $.each(array, function(value) {
      $('.' + value).hide();
    });
  });
 
 
}); 
