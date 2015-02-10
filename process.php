<?php
    $errors         = array();
    $data           = array();

    // validiton for message and anti-spam answer.
    if (empty($_POST['message']))
        $errors['message'] = 'At least say something!';
        
   if($_POST['answerValue'] != $_POST['answerInput'])
      $errors['answerInput'] = 'Answer is not correct.  Try again.';   

    if ( ! empty($errors)) {
        // if there are items in our errors array, return those errors
        $data['success'] = false;
        $data['errors']  = $errors;
    } 
    else {
        // if there are no errors process our form, then return a message
        //process successful post
        $_POST['name'] = filter_var($_POST['name'], FILTER_SANITIZE_STRING);
        $_POST['email'] = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);   
        $_POST['message'] = filter_var($_POST['message'], FILTER_SANITIZE_STRING);  

        $to = 'jack@samueljrains.com';
        $subject = 'New Message from your site';
        $message  = 'From: ' . $_POST['name'] . "\n";
        $message .= 'Email: ' . $_POST['email'] . "\n";
        $message .= "Message:\n" . $_POST['message'] . "\n\n";

       //posts form values if present or generic values if not (so the email looks pretty)
       ($_POST['email'] != null ?   $from = $_POST['email'] : $from = 'no-reply@samueljrains.com');
       ($_POST['name'] != null ?    $name = $_POST['name'] : $name = 'No Name');    
       
       //build array of header values and populate with correct form values from check above   
       $headers   = array();
       $headers[] = "MIME-Version: 1.0";
       $headers[] = "Content-type: text/plain; charset=iso-8859-1";
       $headers[] = "From: " . $name . " <" . $from . ">";
       $headers[] = "Reply-To: Recipient Name <no-reply@samueljrains.com>";
       $headers[] = "Subject: A message from your site!";
       $headers[] = "X-Mailer: PHP/".phpversion();   
       mail($to, $subject, $message, implode("\r\n", $headers));
       // show a message of success and provide a true success variable
       $data['success'] = true;
       $data['message'] = 'Success!';
    }
    // return all our data to an AJAX call
    echo json_encode($data);
?>
