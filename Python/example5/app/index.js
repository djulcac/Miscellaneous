var express = require('express')
var app = express();
var routes = require('./settings/routes');

app.get('/',routes.index);

app.listen(3000,function(){
    console.log('Ejecutando ...')
})