function setRoute(route) {
    window.history.pushState("", "", route); // Last arg is the url extension ex: https://example.com/ + last arg
}