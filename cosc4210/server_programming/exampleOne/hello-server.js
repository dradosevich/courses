//Danny Radosevich
//COSC4210

var http = require("http"), server; //include files in separate modules

//create our server
server = http.createServer(function(req, res)
{
    //write our header in out response, 200 to show it is ok
    //and include the type of content being returned 
    //console.log(req)
    console.log(req.method)
    res.writeHead(200,{"Content-Type":"text/plain"});
    res.end("Hello, class!");
});
//set uo the port  we will lsiten on
server.listen(8080);
console.log("server running on port 8080");