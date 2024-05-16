"use strict";

// 1 - inserir dado
localStorage.setItem("nome", "renan");

// 2 - restart sem perder dados

// 3 - resgatar item
const nome = localStorage.getItem("nome");
console.log(nome);

// 4 - resgate de item que não existe
const lastName = localStorage.getItem("lastname");

console.log(lastName);

if (!lastName) {
  console.log("Sem sobrenome!");
}

// 5 - remover item
localStorage.removeItem("nome");

// 6 - limpar todos os itens
localStorage.setItem("a", 1);
localStorage.setItem("b", 2);
// localStorage.clear();

// 7 - session storage
sessionStorage.setItem("number", 123);

// 8 reiniciar e perder dados
const n = sessionStorage.getItem("number");

console.log(n);

// sessionStorage.removeItem("number");

sessionStorage.clear();

// 9 - salvar objeto

const person = {
  nome: "renan",
  idade: 20,
  trabalho: "Programador",
};

// localStorage.setItem("person", person);

localStorage.setItem("person", JSON.stringify(person));

const getPerson = localStorage.getItem("person");

console.log(getPerson);

const personObject = JSON.parse(getPerson);

console.log(typeof personObject);

console.log(personObject.nome);
