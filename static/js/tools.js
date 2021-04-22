function initializeLoadingScreen(classname) {
    var laoding_box = $("." + classname);
    for (var i = 1; i <= 20; i++) {
        var span = document.createElement('span');
        span.setAttribute("style", `--i:${i};`)
        laoding_box.append(span);
    }
}
function show_loading_screen() {
    $(".loading").css({
        'display':'flex',
        'visibility': 'visible'
    })
}
function hide_loading_screen() {
    $(".loading").fadeOut('fast');
    $(".loading").css({
        'display': 'none',
        'visibility':'hidden'
    });
}