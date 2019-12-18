function initializeMap(objectsList, pinImage) {
    var features = [];

    objectsList.forEach(function (item) {
        features.push(new ol.Feature({
            desc: item.location,
            geometry: new ol.geom.Point(ol.proj.fromLonLat([item.location_lon, item.location_lat]))
        }));
    });
    var layer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: features
        })
    });

    layer.setStyle(new ol.style.Style({
        image: new ol.style.Icon({
            crossOrigin: 'anonymous',
            src: pinImage
        })
    }));

    var view = new ol.View({
        center: ol.proj.fromLonLat([25.6561783, 42.6276194]),
        zoom: 7
    })

    var map = new ol.Map({
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM({
                    "url": "https://maps.wikimedia.org/osm-intl/{z}/{x}/{y}.png"
                })
            }),
            layer
        ],
        target: document.getElementById('map'),
        view: view
    });
    var popup = new ol.Overlay({
        element: document.getElementById('popup')
    });

    map.addOverlay(popup);
    map.on('click', function (evt) {
        var element = popup.getElement();
        $(element).popover('destroy');
        var f = map.forEachFeatureAtPixel(
            evt.pixel,
            function (ft, layer) { return ft; }
        );

        if (map.hasFeatureAtPixel(evt.pixel) === true) {
            var coordinate = f.getGeometry().getCoordinates();
            popup.setPosition(coordinate);
            $(element).popover({
                placement: 'top',
                animation: false,
                html: true,
                content: f.get('desc')
            });
            $(element).popover('show');
            view.animate({ center: coordinate, zoom: 16 });
        }
    });
    $('#osm-map').on('click', function () {
        setTimeout(function () { map.updateSize(); }, 200);
    })
}
