const fs = require('fs');
const path = require('path');

// Get file name from command line arguments
const fileName = process.argv[2];
if (!fileName) {
    console.error("No file name provided!");
    process.exit(1);
}

const filePath = path.join(__dirname, fileName);

try {
    const data = fs.readFileSync(filePath, 'utf8');
    console.log(data); // Output the file content
} catch (err) {
    console.error(`Error reading file: ${err}`);
    process.exit(1);
}
