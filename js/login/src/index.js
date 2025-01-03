const express = require("express");
const path = require("path");
const collection = require("./config");
const bcrypt = require("bcrypt");

const app = express();

// convert data into json format
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Static file
app.use(express.static("public"));

// Use EJS as the view engine
app.set("view engine", "ejs");
app.set("views", "src/views");

app.get("/", (req, res) => {
  res.render("login");
});

app.get("/signup", (req, res) => {
  res.render("signup");
});

app.get("/change-password", (req, res) => {
  res.render("change-password");
});

// Register User
app.post("/signup", async (req, res) => {
  const data = {
    name: req.body.username,
    password: req.body.password,
  };

  // Check if the username already exists in the database
  const existingUser = await collection.findOne({ name: data.name });

  if (existingUser) {
    res.send("User already exists. Please choose a different username.");
  } else {
    // Hash the password using bcrypt
    const saltRounds = 10; // Number of salt rounds for bcrypt
    const hashedPassword = await bcrypt.hash(data.password, saltRounds);

    data.password = hashedPassword; // Replace the original password with the hashed one

    const userdata = await collection.insertMany(data);
    console.log(userdata);
    res.send("User registered successfully!");
  }
});

// Login user
app.post("/login", async (req, res) => {
  try {
    const check = await collection.findOne({ name: req.body.username });
    if (!check) {
      res.send("User name cannot found");
    }
    // Compare the hashed password from the database with the plaintext password
    const isPasswordMatch = await bcrypt.compare(
      req.body.password,
      check.password
    );
    if (!isPasswordMatch) {
      res.send("wrong Password");
    } else {
      res.render("home");
    }
  } catch {
    res.send("wrong Details");
  }
});

// Change Password
app.post("/change-password", async (req, res) => {
  try {
    const { username, oldPassword, newPassword } = req.body;
    const user = await collection.findOne({ name: username });
    if (!user) {
      res.send("User not found");
      return;
    }

    // Compare the old password
    const isOldPasswordMatch = await bcrypt.compare(oldPassword, user.password);
    if (!isOldPasswordMatch) {
      res.send("Old password is incorrect");
      return;
    }

    // Hash the new password
    const saltRounds = 10;
    const hashedNewPassword = await bcrypt.hash(newPassword, saltRounds);

    // Update the user's password in the database
    await collection.updateOne(
      { name: username },
      { $set: { password: hashedNewPassword } }
    );

    res.send("Password changed successfully!");
  } catch (error) {
    res.send("An error occurred while changing the password");
  }
});

// Define Port for Application
const port = 5000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
