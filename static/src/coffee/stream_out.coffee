window.getFinalStatic = ()->
    $.get "/stream_final/1", (data)->
      $( "#description" ).html $(data).find('.table')

# setInterval window.getFinalStatic, 25000
setTimeout window.getFinalStatic, 5000

