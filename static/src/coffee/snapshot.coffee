Webcam.attach '#mycamera'

window.take_snapshot = ()->
	Webcam.snap (data_url)->
		$.post "/validate/photo/", {'image': data_url}, (response)->
			console.log response

setInterval window.take_snapshot, 60000
