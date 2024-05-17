const mongoose = require("mongoose");
const connect = mongoose.connect("mongodb://localhost:27017/test-login");

// Check database connected or not
connect
  .then(() => {
    console.log("Database Connected Successfully");
  })
  .catch((err) => {
    console.log("Database cannot be Connected", err);
  });

// Create Schema
const LoginSchema = new mongoose.Schema({
  name: {
    type: String,
    require: true,
  },
  password: {
    type: String,
    required: true,
  },
});

// Collection part
const collection = new mongoose.model("users", LoginSchema);

module.exports = collection;
