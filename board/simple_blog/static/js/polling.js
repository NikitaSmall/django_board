$(document).ready(function() {
  var messagesCount = $('.message').length;
  var topicId = $('#topic').data('id');
  var author, inner, imageBlock = '';
  var i = 1;

  setInterval(function() {
    $.ajax({
      url: '/topic/' + topicId + '/check'
    }).done(function(data) {
      if (data.length != messagesCount) {
        inner = '';

        for(i = 1; i <= data.length; i++) {
          if (data[i - 1].author.length > 0) {
            author = data[i - 1].author;
          } else {
            author = 'Anonymous';
          }

          if (data[i - 1].docfile) {
            imageBlock = '<div class="clearfix">' +
              '<div class="pull-right">' +
                '<img width="150" src="' + data[i - 1].docfile + '" class="img-rounded">' +
              '</div>' +
            '</div>';
          } else {
            imageBlock = '';
          }


          inner += '<div class="col-md-12 message">' +
            '<div class="panel panel-default">' +
              '<div class="panel-heading">' +
                '<h3 class="panel-title">' +
                  '<strong>' + i + '</strong>:' +
                  author +
                '</h3>' +
              '</div>' +
              '<div class="panel-body">' +
                data[i - 1].text +
                imageBlock +
              '</div>' +
            '</div>' +
          '</div>';
        }
        $('#messages').html(inner);

      }
    });
  }, 1000);
});
