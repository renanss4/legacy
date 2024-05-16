const http = require("http");

const port = 8080;

const server = http.createServer((req, res) => {
  if (req.url === "/") {
    res.writeHead(200, { "Content-Type": "text/html" });
    res.end("<h1>Home Page</h1>");
  }

  if (req.url == "/users") {
    const users = [
      {
        name: "John Doe",
        email: "john@doe.com",
      },
      {
        name: "Jane Doe",
        email: "jane@doe.com",
      },
    ];

    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(users));
  }
});

const execute = (port) => {
  console.log(`Running on port ${port}!`);
  console.log(`Open in your browser: http://127.0.0.1:${port}`);
};

server.listen(port, execute(port));
