$(document).ready(function () {
    var recs = JSON.parse(document.getElementById('recs').textContent); 
    $('.rec-img').css('background-image',`url("${recs}")`);
    $('.rec-img').html('recs');
});