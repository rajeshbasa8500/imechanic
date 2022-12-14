var map;
var geocoder;
function InitializeMap() {

    var latlng = new google.maps.LatLng(17.3522665, 78.5493272);
    var myOptions =
    {
        zoom: 10,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true
    };
    
    map = new google.maps.Map(document.getElementById("map"), myOptions);
}

function FindLocaiton() {
    geocoder = new google.maps.Geocoder();
    InitializeMap();

    var address = document.getElementById("addressinput").value;
    geocoder.geocode({ 'address': address }, function (results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            map.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
            });

        }
        else {
            alert("Geocode was not successful for the following reason: " + status);
        }
    });

}


function Button1_onclick() {
    FindLocaiton();
}

window.onload = InitializeMap;


// let map, infoWindow; 

// function initMap() {
//   map = new google.maps.Map(document.getElementById("map"), {
//     center: { lat: 17.3522665, lng: 78.5493272 },
//     zoom: 15,
//   });
//   function success(position) {
//       var latitude  = position.coords.latitude;
//       var longitude = position.coords.longitude;
//       console.log(latitude, longitude);
  
      
            
            
//              document.getElementById("lat").value = latitude;
//              document.getElementById("lang").value = longitude;
          
   
//       }
  
  
//     navigator.geolocation.getCurrentPosition(success);
//   infoWindow = new google.maps.InfoWindow();

//   const locationButton = document.createElement("button");

//   locationButton.textContent = "Current Location";
//   locationButton.classList.add("custom-map-control-button");
//   map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
//   locationButton.addEventListener("click", () => {
//     // Try HTML5 geolocation.
//     if (navigator.geolocation) {
//       navigator.geolocation.getCurrentPosition(
//         (position) => {
//           const pos = {
//             lat: position.coords.latitude,
//             lng: position.coords.longitude,
//           };
          
//           var icon = {
//               url: "https://img.icons8.com/arcade/100/000000/experimental-marker-arcade.png", // url
//               scaledSize: new google.maps.Size(45, 45), // size
//           };

//           let markerOptions = {
//             position: new google.maps.LatLng(pos),
//             map:map,
//             icon:icon,
//             animation: google.maps.Animation.DROP,
//           }
//           let marker = new google.maps.Marker(markerOptions)
//           marker.setMap(map)
//           map.setCenter(pos)
//           // infoWindow.setPosition(pos);
//           // infoWindow.setContent("Location found.");
//           // infoWindow.open(map);
//           // map.setCenter(pos);
//         },
//         () => {
//           handleLocationError(true, infoWindow, map.getCenter());
//         }
//       );
      
//     } else {
//       // Browser doesn't support Geolocation
//       handleLocationError(false, infoWindow, map.getCenter());
//     }
//   });
// }

// function handleLocationError(browserHasGeolocation, infoWindow, pos) {
//   infoWindow.setPosition(pos);
//   infoWindow.setContent(
//     browserHasGeolocation
//       ? "Error: The Geolocation service failed."
//       : "Error: Your browser doesn't support geolocation."
//   );
//   infoWindow.open(map);
// }

// window.initMap = initMap;