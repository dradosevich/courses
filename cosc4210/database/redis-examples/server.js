//Danny Radosevich
//CSC4210
//Redis example



var express = require("express");
var http = require("http");
var redis = require("redis");
var iored = require("ioredis");
const { getRandomValues } = require("crypto");

var app;
var messages = [{}]
//"vagrant",6379
db_client = redis.createClient();
//db_client.connect()

db_client.connect();
db_client.on('connect', function()
{
    console.log('conencted!')
})
//create our express server, have it listen on port 8080
app = express()
app.use(express.static(__dirname+"/client"));
app.use(express.urlencoded({extended:true}));
http.createServer(app).listen(8080);


async function addToMessages(keys)
{
    for(const key of keys)
    {
        value = await db_client.get(key);
        //addToMessages(element, value);  
        messages.push({[key]:value})
        console.log("Messages currently,",messages)
    }

    /*mongkeys.forEach( async key => 
    {
        value = await db_client.get(key);
        //addToMessages(element, value);  
        messages.push({[key]:value})
        console.log("Messages currently,",messages)
    });*/
}
async function populateMessages()
{
    //return new Promise( async (resolve)=>
    //{ 
        await addToMessages( await db_client.sendCommand(['keys','*']))
        
    //})   
}
async function getMessages()
{
    //keys = await getKeys()
    
    await populateMessages().then(()=>
    {
        console.log("getting messages")
        return messages;
    })
    
}

//now set up our routs 
//responds to  HTTP get requests at url:port/hello
app.get("/todos",async function(req,res)
{
    console.log("Got a get request!");
    //console.log(messages);
    messages = [{}]
    //await getMessages();
    
    await getMessages().then(()=>
        {
            res.json(messages)
            console.log("------------\n",messages)
        }
    )
    //res.json(await getMessages());
});

app.get("/goodbye",function(req,res)
{
    res.send("Goodbye class")
});

app.post("/todos",async function(req,res)
{
    var message = req.body;
    console.log(message);
    messages.push(message);
    for (const[key,value] of Object.entries(message))
    {
        await db_client.set(key,value);
    }
    //
    console.log("got a post request");
    res.json({"message":"You posted to the server"});
});


