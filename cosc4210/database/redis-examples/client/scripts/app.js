//Danny Radosevich
//Example One
//COSC4210 UWYO
//Dialog window

var main = function() 
{
    todos = [{}]
    $.get("todos",function(data)
    {
        data.forEach(function(card)
            {
                /*
                console.log(card.rank+" of "+card.suit);   
                var $card = $("<li>");
                $card.text(card.rank+" of "+card.suit);
                $list.append($card);*/ 
                var $p_body = $("<p>")
                //var $list = $("<ul>");
                for (const[key,value] of Object.entries(card))
                {
                    if(key!=""&&value!="")
                    {
                        //var $todo = $("<li>");
                        $p_body.text(key+":"+value);
                        //$list.append($todo);
                        //$p_body.append($list)
                        $("body").append($p_body)
                        
                    }                    
                }         
                
            });
    })

    "use strict";
    console.log("hi")
    //get the button press information and append the json
    $(".key-input").val("")
    $(".val-input").val("")
    $(".my-input button").on("click",function(event)
    {
        console.log("Made it")
        let to_add_key = $(".key-input").val();
        let to_add_msg = $(".val-input").val();
        $(".my-input input").val("")
        if (to_add_key!="" && to_add_msg!="")
        {
            var $p_body = $("<p>");
            $p_body.text(to_add_key+":"+to_add_msg);
            $("body").append($p_body)
            console.log(to_add_key+":"+to_add_msg);
            var newToDo = {[to_add_key]:to_add_msg}
            todos.push(newToDo)
            $.post("todos",newToDo,function(response)
            {
                console.log("We posted to the server!")
                console.log(response)
            })
        }   
    });
};

$(document).ready(main);