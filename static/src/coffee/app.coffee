$ ->
    $('#student #div_id_avatar, #lector #div_id_avatar').map (i, el)-> 
        console.log el
        $(el).addClass('btn').addClass('btn-primary').prepend('<span>Upload</span>')
