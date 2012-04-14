function noteClickHandlers(get_url) {
    $('.note').click(function() {
        var guid = $(this).attr('rel');
        $.get(get_url + guid + "/", {}, function(data) {
            $('textarea').val(data);
        });
    });
}
