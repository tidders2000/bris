$(function() {
  /*bootsrap popover for chart*/
  $('[data-toggle="popover"]').popover()
  $("#hide").click(function() {
    $(".1").toggle();
  });
  
    $('#fade').hide()
	  
	  $('#alert').mouseover(function(){
	  	 $('#fade').show()
	  })

	  /*hide alert box */
	  $('#fade').click(function() {
	    $('#alert').hide();;
	  });
  
  /*hides holiday on the rota and chat*/
  array = []

    $(".test").each(function() {
      array.push(
       parseInt( $(this).text()));
   console.log(array)
    });
    $("#togg").click(function() { 
      
   $.each( array, function( key, value ) {
     $('.'+value).toggle()

    });
  });
});

 

