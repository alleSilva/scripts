const process = require('process');
const https = require("https")
const fs = require("fs")
let i = parseInt(process.argv[2])

fs.readFile('links.txt', (err, data) => {
  if (err) throw err;
  let urls = data.toString().split('\n')

  https.get(urls[i], function(res) {
    const fileStream = fs.createWriteStream(`M2-aula-${i}.mp4`)
    res.pipe(fileStream)
    fileStream.on("finish", function(){
      fileStream.close()
      console.log("Done!")
    })
  })
});

