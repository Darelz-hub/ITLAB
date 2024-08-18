$(document).ready(function(){
    // Назначим обработчик события на кнопку
    $('#profile_change').on("submit", function(event){
        event.preventDefault(); // Отменяем стандартное поведение формы
        // Получаем данные из полей формы
        const data = {
        email: $("#email").val()
        };
        ProfileChangeFunction(data);
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
                }
            }
        }
    return cookieValue;
}
function ProfileChangeFunction(data){
    $.ajax({
        url: '/users/profile_change/',
        type: 'POST',
        data: data,
        dataType: 'json',
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        },
        success: function(data){
            console.log(data.message);
        },
        error: function(data){
            console.log('Ошибка:', data.error);
        }
    });
}
