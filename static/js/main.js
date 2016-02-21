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
  // $('#form-email').on('submit', onSubmitForm);
  jQuery('#masthead_cta').click(function() {
    jQuery('#masthead').replaceWith($('#masthead_video').show());
    var vi = jQuery("#masthead_yt");
    vi.attr("src",vi.data("autoplay-src"));
  });
});

// Slideshow
$('.gallery').each(function(){
  // scope everything for each slideshow
  var $this = this;
  $('> :gt(0)', $this).hide();
  setInterval(function(){
    $('> :first-child',$this).fadeOut()
      .next().fadeIn().end()
      .appendTo($this);
  }, 3000);
});

// Tabs
$(document).ready(function() {
    $("#tabs-menu a").click(function(event) {
        event.preventDefault();
        $(this).addClass("current");
        $(this).siblings().removeClass("current");
        var tab = $(this).attr("href");
        $(".tab-content").not(tab).css("display", "none");
        $(tab).fadeIn();
    });
});
