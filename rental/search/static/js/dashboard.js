jQuery( document ).ready(function() {
  
	jQuery('#location').click(function(){
 		var ip_location = jQuery('#ip_location').val();
 		$('#search_input').attr('value', '');
 		$('#search_input').attr('value', ip_location);

	});
});
