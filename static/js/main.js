// If Javascript is not enabled and the user submits the form,
// this code never runs, and the form POSTs to the endpoint
// like normal.
onSubmitForm = function(e) {
  // Stop form submission
  e.preventDefault();

  // Extract email address
  $form = $(e.currentTarget);
  emailText = $form.find('input[name=email]').val();
  console.debug("ok, we got " + emailText);

  // Send to server
  // TK

  // Show confirmation
  $form.append("<p class=\"notice\">Thanks, <strong>" + emailText + "</strong>!</p>");
};

jQuery(document).ready(function(){
  jQuery('.gallery').fadeSlideShow();
  $('#form-email').on('submit', onSubmitForm);
});
