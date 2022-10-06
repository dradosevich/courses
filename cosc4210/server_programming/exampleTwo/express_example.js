//Danny Radosevich
//CSC4210
//Express example

var express = require("express");
var http = require("http");
var app;

//create our express server, have it listen on port 8080
app = express();
http.createServer(app).listen(8080)

//now set up our routs 
//responds to  HTTP get requests at url:port/hello
app.get("/hello",function(req,res)
{
    res.send("Hello, class!");
});

app.get("/goodbye",function(req,res)
{
    res.send("Goodbye class")
});

app.get("/",function(req,res)
{
    res.send("root")
});
