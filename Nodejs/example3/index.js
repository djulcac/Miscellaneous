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

async function run(){
    console.log(new Date(),'start');
    const [results, metadata] = await sequelize.query("select * from tem1");
    console.log(1,results)
    console.log(2,metadata)
    console.log(new Date(),'end');
}

run()