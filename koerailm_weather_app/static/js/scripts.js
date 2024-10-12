function user_location() {
    navigator.geolocation.getCurrentPosition(show_location);
}

function show_location(pos) {
    const latitude = pos.coords.latitude;
    const longitude = pos.coords.longitude;

    window.location.href = `?latitude=${latitude}&longitude=${longitude}`;
}