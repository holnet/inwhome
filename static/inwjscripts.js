/* TODO */
function copyToClipboard(element) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $temp.remove();
}

function handleCopyButton(element) {
   $(element).on("click", function(e){
       // was bei einem Klick ausgeführt werden soll
       e.currentTarget.innerHTML = "copied";
   });
   $(element).on("mouseenter", function(e){
       // was beim Eintreten der Maus auf das Element ausgeführt werden soll
       $(this).animate({width: "105px", marginleft:"10px", borderRadius: "50%"}, 500, function(){
            $(this).css("background-color", "white");
        });
       $(this).css("box-shadow", "0px 10px 10px #000000");
   });
   $(element).on("mouseleave", function(e){
        // was beim Austreten der Maus auf das Element ausgeführt werden soll
        $(this).css("background-color", "#7887AB");
        $(this).css("box-shadow", "0px 0px 0px #FFFFFF");
        $(this).animate({width: "100px", marginLeft:"5px", borderRadius: "4px"}, 100);
        e.currentTarget.innerHTML = "Copy";
   });
}