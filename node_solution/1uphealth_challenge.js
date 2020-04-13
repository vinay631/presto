'use strict';

const fs = require('fs');
const presto = require('presto-client');

//Read command line args.
var argv = require('yargs')
    .usage('Usage: node ./$0 [firstName] [lastName]')
    .demandCommand(2)
    .help('h')
    .alias('h', 'help')
    .argv;

const firstName = argv._[0];
const lastName = argv._[1];

// Read presto client config.
const config = require('./config.json');

// Create Presto Client
const client = new presto.Client({
    user: config.default.user,
    host: config.default.host,
    catalog: config.default.catalog,
    schema: config.default.schema
});

// Read allergy information query.
const sql = readAllergyInfoSql(firstName, lastName);

client.execute({
    query: sql,
    catalog: 'hive',
    schema: 'leap',
    state: function (error, query_id, stats) {},
    columns: function (error, data) {},
    data: function (error, data, columns, stats) {
        console.log("Code\t\tDescription");
        for (let result of data) {
            console.log(`${result[0]}\t${result[1]}`);
        }
    },
    success: function (error, stats) {},
    error: function (error) {
        console.log('e', error)
    }
});