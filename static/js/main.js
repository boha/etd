// If Javascript is not enabled and the user submits the form,
// this code never runs, and the form POSTs to the endpoint
// like normal.
onSubmitForm = function(e) {
  // Stop form submission
  e.preventDefault();

  // Extract email address
  var $form     = $(e.currentTarget),
      emailText = $form.find('input[name=email]').val();
  console.debug("ok, we got " + emailText);

  // Send to server
  var csrftoken = $('meta[name=csrf-token]').attr('content');
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
  // TK

  // Show confirmation
  $form.find(".response-msg").html("<p class=\"notice\">Thanks, <strong>" + emailText + "</strong>!</p>");
};

jQuery(document).ready(function(){
  jQuery('.gallery').fadeSlideShow();
  // $('#form-email').on('submit', onSubmitForm);
});
