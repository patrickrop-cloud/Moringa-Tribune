$(document).ready(function(){
    $('form').submit(function(event){
        event.preventDefault()
        form = $("form")

        $.ajax({
            'url':'/ajax/newsletter/',
            'type':'POST',
            'data':form.serialize(),
            'dataType':'json',
            'success': function(data){
                alert(data['success'])
            },
        })//end of Ajax method
        $('#id_your_name').val('')
        $("#id_email").val('')
    })//End of submit event
})//End of document ready funcion