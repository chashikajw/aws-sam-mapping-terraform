var fs = require('fs');

const readfile = (filepath)=> {
    return new Promise((resolve, reject) => {
        fs.readFile(filepath, 'utf8', (err, data) => {
            if(err) {
                reject(err);
            }else {
                resolve(data);
            }
        })
    })   
}
readfile("../SAMmodel.yaml").then(data => {
    const lineArray = data.toString().split('\n');
    lineArray.forEach((line, i) => {
        if(line.includes(":" && ("Resources" || "resources"))){
            const name = lineArray[i+1].trim().substring(0,lineArray[i+1].trim().length-1)
        }
        if(line.includes(":" && ("type" || "Type") && ("function" || "Function"))) {
            const resourceName = "aws_lambda_function";
        }
        if(line.includes(":" && ("Handler" || "handler"))){
            const lambdaName = line.trim().substring(line.trim().indexOf(":")+1, line.trim().length)
        }
        if(line.includes(":" && ("CodeUri" || "codeuri"))) {
            const bucket = line.trim().substring(line.trim().indexOf(":")+1, line.trim().length);
        }
        // console.log(line)
    });
});

const getProvider = (providerName) => {
    return providerName;
}

const getRegion = (region) => {
    return region;
}

const getAccessKey = (AccessKey) => {
    return AccessKey;
}

const getSecretKey = (SecretKey) => {
    return SecretKey;
}
