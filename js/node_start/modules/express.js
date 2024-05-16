const express = require("express");
const UserModel = require("../src/models/user.model");

const port = 8080;

const app = express();

app.use(express.json());

app.set("view engine", "ejs");
app.set("views", "src/views");

app.use((req, res, next) => {
  console.log(`Request Type: ${req.method}`);
  console.log(`Content Type: ${req.headers["content-type"]}`);
  console.log(`Date: ${new Date()}`);

  next();
});

// app.get("/", (req, res) => {
//   res.setHeader("content-type", "text/html");
//   res.status(200).send("<h1>Hello World</h1>");
// });

app.get("/views/users", async (req, res) => {
  const users = await UserModel.find({});

  res.render("index", { users });
});

app.get("/users", async (req, res) => {
  try {
    const users = await UserModel.find({});

    return res.status(200).json(users);
  } catch (error) {
    return res.status(500).send(error.message);
  }
});

app.get("/users/:id", async (req, res) => {
  try {
    const id = req.params.id;

    const user = await UserModel.findById(id);

    return res.status(200).json(user);
  } catch (error) {
    return res.status(500).send(error.message);
  }
});

app.post("/users", async (req, res) => {
  try {
    const user = await UserModel.create(req.body);

    return res.status(201).send(`Usuário ${user.firstName} adicionado!`);
  } catch (error) {
    return res.status(500).send(error.message);
  }
});

app.patch("/users/:id", async (req, res) => {
  try {
    const id = req.params.id;

    const user = await UserModel.findByIdAndUpdate(id, req.body, { new: true });

    return res.status(200).json(user);
  } catch (error) {
    return res.status(500).send(error.message);
  }
});

app.delete("/users/:id", async (req, res) => {
  try {
    const id = req.params.id;

    const user = await UserModel.findByIdAndDelete(id, req.body, { new: true });

    return res.status(200).json(user);
  } catch (error) {
    return res.status(500).send(error.message);
  }
});

app.listen(port, () => {
  console.log(`Running on port ${port}!`);
  console.log(`Open in your browser: http://127.0.0.1:${port} `);
});
