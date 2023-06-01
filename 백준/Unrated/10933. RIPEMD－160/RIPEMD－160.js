const fs = require('fs');
const crypto = require('crypto');

function main() {
    let s = fs.readFileSync('/dev/stdin').toString().trim();

    console.log(crypto.createHash('ripemd160').update(s).digest('hex'));
}

main();