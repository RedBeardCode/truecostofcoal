var max_width = 9204;
var max_height =4647;

var map = L.map('mapid', {
    maxZoom: 7,
    minZoom: 1,
    center: [82, -129],
    zoom:4,
    crs: L.CRS.EPSG3857
});



L.tileLayer(
    '/static/maps/{z}/map_{x}_{y}.png'
    ).addTo(map);


var southWest = map.unproject([0, max_height], map.getMaxZoom());
var northEast = map.unproject([max_width, 0], map.getMaxZoom());
map.setMaxBounds(new L.LatLngBounds(southWest, northEast));


L.control.mousePosition().addTo(map);

// var statesData = {
//     "type": "FeatureCollection", "features": [
//         {
//             "type": "Feature",
//             "id": "01",
//             "properties": {"name": "Alabama", "density": 1000.65},
//             "geometry": {
//                 "type": "Polygon",
//                 // "coordinates": [[
//                 //     [70.359296, -5.00118],
//                 //     [50.606675, -4.984749],
//                 //     [50.431413, -4.124869],
//                 //     [70.359296, -5.00118]
//                 // ]]
//                 // "coordinates":[[
//                 //     [84.4, -160],
//                 //     [74.2, -150],
//                 //     [74.5, -160],
//                 //     [84.4, -160]
//                 // ]]
//                  "coordinates":[[
//                     [-116.322, 84.48545],
//                     [-113.421, 84.2746],
//                     [-113.289, 84.48545],
//                     [-116.322, 84.48545]
//                 ]]
//                 // "coordinates":[[
//                 //     [12927138.912388057, 19347678.31363939],
//                 //     [-12631174.738867857, 19126316.67972551],
//                 //     [-12626282.769057605, 19373361.1551432],
//                 //     [-12927138.912388057, 19347678.31363939]
//                 // ]]
//             }
//         }
//     ]
// };

function highlightFeature(e, o) {
    var layer = e.target;

    layer.setStyle({
        weight: 0,
        fillOpacity: o
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
};


function zoomToFeature(e) {
		map.fitBounds(e.target.getBounds());
	};



function onEachFeature(feature, layer) {
		layer.on({
			"mouseover": function(e){highlightFeature(e, 0.5);},
			"mouseout": function(e){highlightFeature(e, 0);},
			click: zoomToFeature
		});

	};

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

var geojson = 0;
$.ajax({
  url: "/",
  type: "POST",
  cache: false,
  success: function(regiondata){

        geojson = L.geoJson(regiondata, {
             style: {weight: 0,fillOpacity:0 },
             onEachFeature: onEachFeature
        });
        map.addLayer(geojson);

  }
});





