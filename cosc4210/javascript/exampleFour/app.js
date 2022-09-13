//Danny Radosevich
//Example One
//COSC4210 UWYO
//Dialog window



var main = function() 
{
    "use strict";
    
    var addComment = function()
    {
        if ($(".comment-input input").val() !=="")
        {
            var $new_comment = $("<p>").text($(".comment-input input").val());
            $new_comment.hide();
            $(".comments").append($new_comment);
            $new_comment.fadeIn();
            $(".comment-input input").val("");
        }
    }

    $(".comment-input button").on("click",function(event)
    {
         addComment();
    });
    $(".comment-input input").on("keypress", function(event)
    {
        if ($(".comment-input input").val() !=="" && event.keyCode==13)
        {
            addComment();
        } 
    });
    
};

