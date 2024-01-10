const fs = require('fs');
const path = require('path');

// Function to read file content
function readFileContent(filePath) {
    try {
        // Read file content
        const data = fs.readFileSync(filePath, 'utf8');
        console.log(`File content of ${filePath}:`);
        console.log(data);

        // Here you can add more logic to process the file content
        // For example, sending it to an API, processing the data, etc.

    } catch (err) {
        console.error(`Error reading file from disk: ${err}`);
    }
}

// Specify the path to your file
// Replace 'your/file/path.txt' with the path to the file you want to read
const filePath = path.join(__dirname, 'your/file/path.txt');

// Read the file
readFileContent(filePath);
