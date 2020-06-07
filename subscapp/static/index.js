$(document).ready(function () {
    var recs = JSON.parse(document.getElementById('recs').textContent); 
    var go = 'huhu'
    $('.rec-img').css('background-image',`url("${recs}")`);
    
});