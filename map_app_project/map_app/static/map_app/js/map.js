// map_app/static/map_app/map.js
document.addEventListener('DOMContentLoaded', function() {
    const mapOptions = {
        center: new google.maps.LatLng(51.508742, -0.120850),
        zoom: 5,
    };
    const map = new google.maps.Map(document.getElementById('googleMap'), mapOptions);
});
