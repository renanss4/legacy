"use strict";

const nomeForm = document.querySelector("#nome-form");
const welcomeContainer = document.querySelector("#welcome");
const logoutBtn = document.querySelector("#logout");

function checkUser() {
  const userName = localStorage.getItem("nome");

  if (userName) {
    nomeForm.style.display = "none";
    welcomeContainer.style.display = "block";

    const userNameElement = document.querySelector("#username");

    userNameElement.textContent = userName;
  } else {
    nomeForm.style.display = "block";
    welcomeContainer.style.display = "none";
  }
}

nomeForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const nomeInput = document.querySelector("#nome");

  localStorage.setItem("nome", nomeInput.value);

  nomeInput.value = "";

  checkUser();
});

logoutBtn.addEventListener("click", () => {
  localStorage.removeItem("nome");

  checkUser();
});

checkUser();
