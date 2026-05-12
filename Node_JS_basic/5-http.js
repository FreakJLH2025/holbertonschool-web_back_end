// 5-http.js

const http = require('http');
const url = require('url');
const fs = require('fs');

const port = 1245;
const database = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      if (lines.length <= 1) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const students = lines.slice(1).filter((line) => line.trim() !== '');
      const fields = {};

      students.forEach((line) => {
        const parts = line.split(',');
        const firstName = parts[0].trim();
        const field = parts[3].trim();

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      });

      let output = `Number of students: ${students.length}\n`;
      Object.keys(fields).forEach((field) => {
        output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      });

      resolve(output.trim());
    });
  });
}

const app = http.createServer((req, res) => {
  const pathName = url.parse(req.url).pathname;
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (pathName === '/') {
    res.end('Hello Holberton School!');
  } else if (pathName === '/students') {
    res.write('This is the list of our students\n');
    countStudents(database)
      .then((output) => {
        res.end(output);
      })
      .catch((err) => {
        res.end(err.message);
      });
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(port);

module.exports = app;
