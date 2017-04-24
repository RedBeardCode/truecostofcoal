var max_width = 9204;
var max_height =4647;

var map = L.map('mapid', {
    maxZoom: 7,
    minZoom: 1,
    // center: [2323, 4602],
    center: [17, 35],
    zoom:4,
    // crs: L.CRS.Simple
    crs: L.CRS.EPSG4326
});
// var sw = map.unproject([0, max_height], 1);
// var ne = map.unproject([max_width, 0], 1);
// var layerbounds = new L.LatLngBounds(sw, ne);
L.tileLayer(
    'static/maps/{z}/map_{x}_{y}.png'
    ).addTo(map);
var southWest = map.unproject([0, max_height], map.getMaxZoom());
var northEast = map.unproject([max_width, 0], map.getMaxZoom());
map.setMaxBounds(new L.LatLngBounds(southWest, northEast));


L.control.mousePosition().addTo(map);

var statesData = {
    "type": "FeatureCollection", "features": [
        {
            "type": "Feature",
            "id": "01",
            "properties": {"name": "Alabama", "density": 1000.65},
            "geometry": {
                "type": "Polygon",
                // "coordinates": [[
                //     [70.359296, -5.00118],
                //     [50.606675, -4.984749],
                //     [50.431413, -4.124869],
                //     [70.359296, -5.00118]
                // ]]
                "coordinates":[[
                    [-16417450.341062, 17924177.04235],
                              [-13619243.6101, 17239301.269038],
                              [-15849981.843175, 18843867.366512],
                              [-17258869.148275, 19274360.709737],
                                [-16417450.341062, 17924177.04235]
                ]]
            }
        }
    ]
};

function highlightFeature(e, o) {
    var layer = e.target;

    layer.setStyle({
        weight: 0,
        fillOpacity: o
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}


function zoomToFeature(e) {
		map.fitBounds(e.target.getBounds());
	}

function onEachFeature(feature, layer) {
		layer.on({
			mouseover: function(e){highlightFeature(e, 1);},
			mouseout: function(e){highlightFeature(e, 0);},
			click: zoomToFeature
		});
	}

	geojson = L.geoJson(statesData, {
		 style: {weight: 0,fillOpacity: 0.0},
		onEachFeature: onEachFeature
	}).addTo(map);