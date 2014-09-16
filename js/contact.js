// wait for the DOM to be loaded 
$(document).ready(function() {  
    $("#myForm").submit(function(){
        if($.trim($('#message').val()) === ''){
				alertify.error("At least say something!");			
            return(false);
        }
        if($('#answer_value').val() != $('#answer_input').val()) {
				alertify.error("Anti spam answers do not match.");			
           return(false);
        }
    });    
    $('#myForm').ajaxForm(function() { 
        $('#myForm').trigger("reset"); 
        alertify.success("Message sent.  Thank you!");
    }); 
}); 