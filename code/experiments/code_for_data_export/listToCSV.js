var fs  = require("fs");

fs.readFileSync('./my_video.txt').toString().split('\n').forEach(function (line) { 
    line = line.replace(/\[/g, "")
    line = line.replace(/\]/g, "")
    line = line.replace(/\),/g, ";")
    fs.appendFileSync("./output.txt", line.toString() + "\n");
});