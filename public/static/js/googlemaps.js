conf = {
	position: 	[47.16750, 0.59308],
	zoom:		11,
	markers: [{
		title:		'Located item',
		position:	[47.16750, 0.59308],
		icon:		'/static/images/map-icon.png',
		body:		"This is a located item"
	}]
};

$(document).ready(function($){
	var map = new google.maps.Map($('#map').get(0), {
	  zoom: 		conf.zoom,
	  center: 	new google.maps.LatLng(conf.position[0], conf.position[1]),
	  mapTypeId: 	google.maps.MapTypeId.ROADMAP
	});
	
	var marker, win;
	for(i in conf.markers) {
		marker_conf = conf.markers[i];
		marker = new google.maps.Marker({
		  position: new google.maps.LatLng(marker_conf.position[0], marker_conf.position[1]),
		  map:		map,
		  title:	marker_conf.title,
		  icon:		marker_conf.icon
		});
		win = new google.maps.InfoWindow({
			content: "<h3>"+marker_conf.title+"</h3>"+"<p>"+marker_conf.body+"</p>"
		});
		marker.win = win;
		marker.func = function() {
		   this.win.open(map, this);
		}
		google.maps.event.addListener(marker, 'click', marker.func);
	}
});