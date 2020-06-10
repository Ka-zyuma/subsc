$(document).ready(function () {
    var recs = JSON.parse(document.getElementById('recs').textContent);
    var go = 'huhu'
    $('.rec-img').css('background-image', `url("${recs}")`);
    if (sessionStorage.scrollTop != "undefined") {
        $(window).scrollTop(sessionStorage.scrollTop);
    }
    //行き詰まり
    //$('#delete').click(function() {
    // sessionStorage.scrollTop = $(this).scrollTop();
    //});
});
//行き詰まり
//$('#delete').click(function() {
//sessionStorage.scrollTop = $(this).scrollTop();
//});