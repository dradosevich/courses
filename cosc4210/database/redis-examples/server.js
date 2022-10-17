//Danny Radosevich
//CSC4210
//Express example

var express = require("express");
var http = require("http");
var redis = require("redis");
var app;
var messages = [{}]
//"vagrant",6379
db_client = redis.createClient();
//db_client.connect()

db_client.connect();
//create our express server, have it listen on port 8080
app = express()
app.use(express.static(__dirname+"/client"));
app.use(express.urlencoded({extended:true}));
http.createServer(app).listen(8080);


//now set up our routs 
//responds to  HTTP get requests at url:port/hello
app.get("/todos",function(req,res)
{
    console.log("Got a get request");
    console.log(messages)
    res.json(messages);
});

app.get("/goodbye",function(req,res)
{
    res.send("Goodbye class")
});

app.post("/todos",function(req,res)
{
    var message = req.body;
    console.log(message);
    messages.push(message);
    for (const[key,value] of Object.entries(message))
    {
        db_client.set(message);
    }
    //
    console.log("got a post request");
    res.json({"message":"You posted to the server"});
});


