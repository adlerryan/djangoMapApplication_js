function toggleMenu() {
    const menu = document.getElementById('menu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
}
var locations = JSON.parse('{{ locations|escapejs }}');
function initMap() {
    const unionSquare = { lat: 40.7359, lng: -73.9911 };  // Union Square, NYC
    const mapOptions = {
        center: unionSquare,
        zoom: 15,
        disableDefaultUI: true,
        styles: [
            { elementType: "geometry", stylers: [{ color: "#242f3e" }] },
            { elementType: "labels.text.stroke", stylers: [{ color: "#242f3e" }] },
            { elementType: "labels.text.fill", stylers: [{ color: "#746855" }] },
            {
                featureType: "administrative.locality",
                elementType: "labels.text.fill",
                stylers: [{ color: "#d59563" }],
            },
            {
                featureType: "poi", // Hides points of interest
                stylers: [{ visibility: "off" }],
            },
            {
                featureType: "poi.park",
                elementType: "geometry",
                stylers: [{ color: "#263c3f" }],
            },
            {
                featureType: "poi.park",
                elementType: "labels.text.fill",
                stylers: [{ color: "#6b9a76" }],
            },
            {
                featureType: "road",
                elementType: "geometry",
                stylers: [{ color: "#38414e" }],
            },
            {
                featureType: "road",
                elementType: "geometry.stroke",
                stylers: [{ color: "#212a37" }],
            },
            {
                featureType: "road",
                elementType: "labels.text.fill",
                stylers: [{ color: "#9ca5b3" }],
            },
            {
                featureType: "road.highway",
                elementType: "geometry",
                stylers: [{ color: "#746855" }],
            },
            {
                featureType: "road.highway",
                elementType: "geometry.stroke",
                stylers: [{ color: "#1f2835" }],
            },
            {
                featureType: "road.highway",
                elementType: "labels.text.fill",
                stylers: [{ color: "#f3d19c" }],
            },
            {
                featureType: "transit",
                elementType: "geometry",
                stylers: [{ color: "#2f3948" }],
            },
            {
                featureType: "transit.station",
                elementType: "labels.text.fill",
                stylers: [{ color: "#d59563" }],
            },
            {
                featureType: "water",
                elementType: "geometry",
                stylers: [{ color: "#17263c" }],
            },
            {
                featureType: "water",
                elementType: "labels.text.fill",
                stylers: [{ color: "#515c6d" }],
            },
            {
                featureType: "water",
                elementType: "labels.text.stroke",
                stylers: [{ color: "#17263c" }],
            },
            {
                featureType: "administrative.neighborhood", // Show neighborhoods
                elementType: "labels.text.fill",
                stylers: [{ color: "#d59563" }],
            },
            {
                featureType: "administrative.locality", // Show localities (towns and cities)
                elementType: "labels.text.fill",
                stylers: [{ color: "#d59563" }],
            }
            ],
    };
    const map = new google.maps.Map(document.getElementById('googleMap'), mapOptions);

    locations.forEach(location => {
        const marker = new google.maps.Marker({
            position: { lat: parseFloat(location.fields.lat), lng: parseFloat(location.fields.lng) },
            map: map,
            title: location.fields.name,
        });

        google.maps.event.addListener(marker, 'click', function() {
            // Update the modal title
            document.getElementById('locationModalLabel').innerText = location.fields.name;

            // Update the location details
            document.getElementById('locationName').innerText = location.fields.name;

            // Check if image properties are available before setting it
            var imageUrl = "";
            if (location.fields.images && location.fields.images.length > 0 && location.fields.images[0].fields) {
                imageUrl = location.fields.images[0].fields.image_url || "";  // If image_url is undefined, set it to empty string
            } 
            document.getElementById('locationImage').src = imageUrl;
            
            document.getElementById('locationRating').innerText = 'Rating: ' + location.fields.rating;  // Assuming rating is available
            document.getElementById('locationAddress').innerText = 'Address: ' + location.fields.address;  // Assuming address is available

            // Show the modal
            $('#locationModal').modal('show');
        });

    });
}
</script>