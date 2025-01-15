$(document).ready(function() {
    $('#main-contact-form').on('submit', function(e) {
        e.preventDefault();
        
        var form = $(this);
        var url = form.attr('action');
        var csrfToken = form.find('input[name="csrfmiddlewaretoken"]').val();
        
        $.ajax({
            type: 'POST',
            url: url,
            data: form.serialize(),
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: function(response) {
                // Очищаем предыдущие сообщения
                $('.alert').remove();
                
                // Добавляем новое сообщение
                var alertHtml = '<div class="alert alert-' + response.status + '">' + 
                               response.message + '</div>';
                form.prepend(alertHtml);
                
                if (response.status === 'success') {
                    // Очищаем форму при успешной отправке
                    form[0].reset();
                }
                
                // Плавно прокручиваем к сообщению
                $('html, body').animate({
                    scrollTop: form.offset().top - 100
                }, 500);
            },
            error: function() {
                // Очищаем предыдущие сообщения
                $('.alert').remove();
                
                // Добавляем сообщение об ошибке
                var alertHtml = '<div class="alert alert-danger">' + 
                               'Произошла ошибка при отправке сообщения. Пожалуйста, попробуйте позже.' + 
                               '</div>';
                form.prepend(alertHtml);
            }
        });
    });
});
