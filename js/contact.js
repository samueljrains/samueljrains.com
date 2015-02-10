//js to get formData, process form via AJAX, and return success/errors when necessary.
$(document).ready(function() {
    // process the form
    $('form').submit(function(event) {
        var formData = {
            'name'        : $('input[name=name]').val(),
            'email'       : $('input[name=email]').val(),         
            'message'     : $('textarea[name=message]').val(),
            'answerValue' : $('input[name=answerValue]').val(),           
            'answerInput' : $('input[name=answerInput]').val()
        };
        // make AJAX call to PHP program that checks the input values, and anti-spam answers and returns corresponding JSON string. 
        $.ajax({
            type        : 'POST',
            url         : 'process.php',
            data        : formData,
            dataType    : 'json',
            encode      : true
        })
        .done(function(data) {
            if (!data.success) {
                if (data.errors.message) {
                    alertify.error(data.errors.message);
                }
                if (data.errors.answerInput) {
                    alertify.error(data.errors.answerInput);
                }
            } 
            else {
                //success so form is reset and user is notified via alert.
                $('form').trigger("reset"); 
                alertify.success("Message sent.  Thank you!");                  
            }
        })
        .fail(function() {
            alertify.error("Something went wrong.  Try again later.");
            //TODO: call to php function errorLog to log error.
            //console.log(data);
        });
        // stop the form from submitting the normal way and refreshing the page
        event.preventDefault();
    });
}); 