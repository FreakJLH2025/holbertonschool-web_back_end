#!/usr/bin/env node

const express = require('express');
const fs = require('fs');

const app = express();

const database = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .filter((line) => line.trim() !== '');

      const students = lines.slice(1);

      const fields = {};

      students.forEach((student) => {
        const values = student.split(',');
        const firstName = values[0];
        const field = values[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstName);
      });

      const output = [];

      output.push(`Number of students: ${students.length}`);

      Object.keys(fields).forEach((field) => {
        output.push(
          `Number of students in ${field}: ${fields[field].length}. `
          + `List: ${fields[field].join(', ')}`,
        );
      });

      resolve(output.join('\n'));
    });
  });
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(database)
    .then((students) => {
      res.send(`This is the list of our students\n${students}`);
    })
    .catch(() => {
      res.send('This is the list of our students\nCannot load the database');
    });
});

app.listen(1245);

module.exports = app;
