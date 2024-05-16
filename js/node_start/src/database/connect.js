const mongoose = require("mongoose");

const connectToDatabase = async () => {
  try {
    // await mongoose.connect(
    //   `mongodb+srv://${process.env.MONGODB_USERNAME}:${process.env.MONGODB_PASSWORD}@${process.env.MONGODB_URL}`
    // );
    await mongoose.connect(
      `mongodb://${process.env.MONGODB_URL}/${process.env.MONGODB_DATABASE}`
    );
    console.log("Conexão ao banco de dados realizada com sucesso!");

    // Listar as coleções disponíveis no banco de dados
    // const collections = await mongoose.connection.db
    //   .listCollections()
    //   .toArray();
    // console.log("Coleções disponíveis:");
    // collections.forEach((collection) => {
    //   console.log(collection.name);
    // });
  } catch (error) {
    console.error(
      "Ocorreu um erro ao se conectar com o banco de dados:",
      error
    );
  }
};

module.exports = connectToDatabase;
