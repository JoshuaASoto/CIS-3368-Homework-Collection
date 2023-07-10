// load the things we need
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');

// required module to make calls to a REST API
const axios = require('axios');
const res = require('express/lib/response');


app.use(bodyParser.urlencoded());




// set the view engine to ejs
app.set('view engine', 'ejs');



// use res.render to load up an ejs view file
app.use(express.static('public'));
app.use('/css',express.static(__dirname + 'public/css'))





// index page 
app.get('/', function(req, res) {

//render index
    res.render('pages/index', {
 

    });
});

//Login page , runs when info submitted
app.post('/proccessform', function(req,res){
    //Login credentials
    var username = req.body.username;
    var password = req.body.password;

    if (username == "username" && password == "password")
    {
        res.render("pages/home", {
        })
    }
});

// trips page 
app.get('/trips', function(req, res) {

    //API call to trip and destinatiopn tables
    axios.get('http://127.0.0.1:5000/api/viewtrip')
    .then((response)=>{
        //creates array based on trip table
        var trips = response.data;
        console.log(trips);
    
        res.render('pages/trips', { trips: trips });
        
    })


});

// trip page 
app.get('/trips', function(req, res) {

    axios.get('http://127.0.0.1:5000/api/viewtrip')
    .then((response)=>{
        //trip array
        var trips = response.data;
        console.log(trips);

        res.render('pages/trips', {trips:trips});
 
    })
});

// destination page 
app.get('/destinations', function(req, res) {

    axios.get('http://127.0.0.1:5000/api/viewdestination')
    .then((response)=>{
        //destinations array
        var dests = response.data;
        console.log(dests);

        res.render('pages/destinations', {dests:dests});
 
    })
});

// home page 
app.get('/home', function(req, res) {

    res.render('pages/home', {
 
    });
});


// edit trip page
app.get('/edittrip', function(req, res) {

    res.render('pages/edittrip', {
 
    });
});


//Form action Add trip
app.post('/addTrip', function(req,res){

    //Add trip var
    var addID = req.body.addid
    var addT = req.body.addt
    var addS = req.body.adds
    var addE = req.body.adde
    var addN = req.body.addn

    axios.post('http://127.0.0.1:5000/api/addtrip',{
        destinationid: addID,
        transportation: addT,
        startdate: addS,
        enddate: addE,
        tripname: addN
    })
    .then(function (response) {
        console.log(response);
    })
});

//Form Action Edit Trip 
app.post('/editTrip', function(req,res){

    //Edit Trip var
    var updateID = req.body.updateid
    var updateI = req.body.updatedi
    var updateCo = req.body.updatet
    var updateS = req.body.updates
    var updateE = req.body.updatee
    var updateN = req.body.updaten

    axios.post('http://127.0.0.1:5000/api/updatetrip',{

        id:updateID,
        destinationid: updateI,
        transportation: updateCo,
        startdate: updateS,
        enddate: updateE,
        tripname: updateN
    })
    .then(function (response) {
        console.log(response);
    })
});

//Delete Trip
app.post('/deleteTrip', function(req,res){

    //Delete Dest var
    var Delete = req.body.delete
  

    axios.delete('http://127.0.0.1:5000/api/deletetrip/', {data:{id:Delete}})
    .then(function (response) {
        console.log(response);
    })
});


// edit destination page
app.get('/editdest', function(req, res) {
    //page render
    res.render('pages/editdest', {
 
    });
});


//Form action add destination
app.post('/addDestination', function(req,res){

    //Add Dest var
    var addCo = req.body.addco
    var addCi = req.body.addci
    var addSi = req.body.addsi

    axios.post('http://127.0.0.1:5000/api/adddestination',{
        country: addCo,
        city: addCi,
        sightseeing: addSi
    })
    .then(function (response) {
        console.log(response);
    })
});

// Form action edit destination
app.post('/editDestination', function(req,res){

    //Edit Dest var
    var updateI = req.body.updatei
    var updateCo = req.body.updateco
    var updateCi = req.body.updateci
    var updateSi = req.body.updatesi

    axios.post('http://127.0.0.1:5000/api/updatedestination',{

        id: updateI,    
        country: updateCo,
        city: updateCi,
        sightseeing: updateSi
    })
    .then(function (response) {
        console.log(response);
    })
});

// Form action delete destination
app.post('/deleteDestination', function(req,res){

    //Delete Dest var
    var deleteI = req.body.deletei
  

    axios.delete('http://127.0.0.1:5000/api/deletedestination/',{data:{detinationid:deleteI}})
    .then(function (response) {
        console.log(response);
    })
});






//reference https://axios-http.com/docs/api_intro
// https://blog.logrocket.com/understanding-axios-post-requests/
app.listen(8080);
console.log('8080 is the magic port');
