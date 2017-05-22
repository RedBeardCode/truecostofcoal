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



var geojson = 0;
function addRegionsLayer() {
    $.ajax({
        url: "/",
        type: "POST",
        data: {zoomlevel: map.getZoom()},
        cache: false,
        success: function (regiondata) {

            geojson = L.geoJson(regiondata, {
                style: {weight: 0, fillOpacity: 0},
                onEachFeature: onEachFeature
            });
            map.addLayer(geojson);

        }
    });
};


function zoomLevelChanged(event)
{
    geojson.remove();
    addRegionsLayer();

};

addRegionsLayer();
map.on('zoomend', zoomLevelChanged);


