var mysql = require('mysql');

var con = mysql.createConnection({
    host: "cis3368.c46eqokjvltp.us-east-2.rds.amazonaws.com",
    user: "admin",
    password: "Technologic7!"
  });

  con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
  });

  