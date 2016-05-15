timeOut = ''

$('#form').submit (e)->
        e.preventDefault()
        $('#captchaSubmit').modal('hide');
        clearTimeout timeOut
        $.post "validate/photo/", $(@).serialize(), (response)->
            console.log response

Webcam.attach '#mycamera'

window.take_snapshot = ()->
    Webcam.snap (data_url)->
        $.post "/validate/photo/", {'image': data_url}, (response)->
            console.log response

window.take_captcha = ()->
    $('#captchaSubmit').modal()
    timeOut = setTimeout $.post("/validate/captcha/", {here: false}), 5000

setInterval window.take_snapshot, 20000
setInterval window.take_captcha, 60000
