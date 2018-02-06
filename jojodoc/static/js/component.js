$(document).ready(function(){
    $("text").hover(function(){
        $("#summaryblock1").attr({
            "fill": "white",
            "stroke": '#F7941E',
            'stroke-width':'2',
            "stroke-miterlimit":'10' 
        });
    })
});