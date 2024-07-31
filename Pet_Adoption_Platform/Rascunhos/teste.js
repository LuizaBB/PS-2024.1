const fs=require('fs')
fs.readFile('testread.txt', 'utf8', (err, data) =>{
    if(err){
        console.error (err)
        return
    }
    console.log(data)
})
console.log(fs.readFileSync("testread.txt", 'utf8'))
fs.appendFileSync("testread.txt", "tudo bem")
console.log(fs.readFileSync("testread.txt", 'utf8'))
fs.writeFileSync("testread.txt", "substituindo o text\nadcionando texto com a função de escrita\n")
// \n funciona como EOF para .txt

var content =fs.readFileSync("testread.txt", 'utf8')
console.log(content)
var result=content.search("adcionando")
console.log(result)

const variable= fs.createReadStream("testread.txt", 'utf8')