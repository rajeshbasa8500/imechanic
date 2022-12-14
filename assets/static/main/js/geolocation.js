// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.
let map, infoWindow; 

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 17.3522665, lng: 78.5493272 },
    zoom: 15,
  });
   
  infoWindow = new google.maps.InfoWindow();

  const locationButton = document.createElement("button");

  locationButton.textContent = "Allow Current Location";
  locationButton.classList.add("custom-map-control-button");
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
  locationButton.addEventListener("click", () => {
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          };
          function success(position) {
            var latitude  = position.coords.latitude;
            var longitude = position.coords.longitude;
            console.log(latitude, longitude);
        
            
                  
                  
                   document.getElementById("latitude").value = latitude;
                   document.getElementById("longitude").value = longitude;
                
         
            }
        
        
          navigator.geolocation.getCurrentPosition(success);
          var icon = {
              url: "https://img.icons8.com/color/48/000000/visit.png", // url
              scaledSize: new google.maps.Size(45, 45), // size
          };

          let markerOptions = {
            position: new google.maps.LatLng(pos),
            map:map,
            icon:icon,
            // animation: google.maps.Animation.DROP,
          }
          let marker = new google.maps.Marker(markerOptions)
          marker.setMap(map)
          map.setCenter(pos)
          // infoWindow.setPosition(pos);
          // infoWindow.setContent("Location found.");
          // infoWindow.open(map);
          // map.setCenter(pos);
        },
        () => {
          handleLocationError(true, infoWindow, map.getCenter());
        }
      );
      
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
    }
  });
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(
    browserHasGeolocation
      ? "Error: The Geolocation service failed."
      : "Error: Your browser doesn't support geolocation."
  );
  infoWindow.open(map);
}

window.initMap = initMap;