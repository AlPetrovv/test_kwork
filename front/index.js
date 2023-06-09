import express from "express";
import path from "path";
import http from "http";
const app = express();
const _http = http.Server(app);
const __dirname = path.resolve();
app.get('/', function (req, res) {
     res.sendFile(__dirname + '/index.html');
});
var port = 3000;
_http.listen(port, function () {
     console.log('ready');
     });
