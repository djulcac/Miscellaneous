const { Sequelize } = require('sequelize');

const sequelize = new Sequelize(
    'postgres', // database
    'postgres', // username
    'postgres', // password
    {
        host: 'localhost',
        dialect: 'postgres',
        logging: false
    }
);

