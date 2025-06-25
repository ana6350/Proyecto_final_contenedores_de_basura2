var mapContainer = document.getElementById('map');

if (mapContainer) {
    var map = L.map('map').setView([4.7423251, -74.115069], 15);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    // Página: /mapa → permitir clic para registrar punto
    if (window.location.pathname.includes("mapa")) {
        map.on('click', function(e) {
            L.marker(e.latlng).addTo(map);
            console.log("Lat:", e.latlng.lat, "Lng:", e.latlng.lng);
        });
    }

    // Página: /about → mostrar polígono de Tibabuyes
    if (window.location.pathname.includes("about")) {
        var latlngs = [
            [4.7423251, -74.115069],
            [4.7435000, -74.114000],
            [4.7450000, -74.113500],
            [4.7440000, -74.116000],
            [4.7423251, -74.115069]
        ];

        var polygon = L.polygon(latlngs, {
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.4
        }).addTo(map);

        map.fitBounds(polygon.getBounds());
    }

    // Página: / → descripción con marcador
    if (window.location.pathname === "/" || window.location.pathname.includes("index")) {
        L.marker([4.7423251, -74.115069])
            .addTo(map)
            .bindPopup('Zona de estudio: Tibabuyes II')
            .openPopup();
    }
}
