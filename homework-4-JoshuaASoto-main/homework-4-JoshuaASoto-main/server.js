// load the things we need
var express = require('express');
var app = express();

// set the view engine to ejs
app.set('view engine', 'ejs');


app.use(express.static('public'));
app.use('/css',express.static(__dirname + 'public/css'))


// index page 
app.get('/', function(req, res) {
    res.render('pages/index', {
    });
});

// recipe page
app.get('/recipe', function(req, res) {
    res.render('pages/recipe');
});

// store page
app.get('/store', function(req, res) {
    res.render('pages/store');
});

// about page
app.get('/community', function(req, res) {
    res.render('pages/community');
});

app.listen(8080);
console.log('8080 is the magic port');
