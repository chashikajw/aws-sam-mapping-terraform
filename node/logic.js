var fs = require('fs');

const readfile = (filepath)=> {
    fs.readFile(filepath, 'utf8', (err, data) => {
        if(err) {
            console.log(err);
        }else {
            console.log(data);
        }
    })
}
// readfile("../lamda.js")