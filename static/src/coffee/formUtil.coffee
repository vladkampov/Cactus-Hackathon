$ ->
    $('#student #div_id_avatar, #lector #div_id_avatar').map (i, el)-> 
        $(el).addClass('btn').addClass('btn-primary').prepend('<span>Upload</span>')
