timeOut = ''

$('form').submit (e)->
    e.preventDefault()
    $('#captchaSubmit').modal('hide');
    clearTimeout timeOut
    $.post "/validate/captcha/", {'form': $(@).serialize(), 'object': object}, (response)->
        if response.captcha is true
            $('#log').append('<span class="alert-success">captcha identify: ' + response.captcha + '</span></br>')
        else
            $('#log').append('<span class="alert-danger">captcha identify: ' + response.captcha + '</span></br>')
    grecaptcha.reset()

Webcam.attach '#mycamera'

window.take_snapshot = ()->
    Webcam.snap (data_url)->
        $.post "/validate/photo/", {'image': data_url, 'object': object}, (response)->
            if response.identical is true
                $('#log').append('<span class="alert-success">Face identify: ' + response.identical + '</span></br>')
            else
                $('#log').append('<span class="alert-danger">Face identify: ' + response.identical + '</span></br>')

window.falseCaptchaTimeout = ()->
    $('#captchaSubmit').modal('hide');
    grecaptcha.reset()
    return $.post("/validate/captcha/", {here: false, 'object': object})

window.take_captcha = ()->
    $('#captchaSubmit').modal()
    timeOut = setTimeout window.falseCaptchaTimeout, 60000

window.getFinalStatic = ()->
    $.get "/stream_final/1", (data)->
      $( "#description" ).html $(data).find('.table')

setInterval window.take_snapshot, 20000
setInterval window.take_captcha, 60000
setInterval window.getFinalStatic, 25000

