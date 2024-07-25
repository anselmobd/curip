django.jQuery(document).ready(function( $ ) {
  $( "#id_sigla" ).bind("input", function() {
    this.value = this.value.toUpperCase();
  });
});
