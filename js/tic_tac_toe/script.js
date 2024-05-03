"use strict";

const resetButton = document.getElementById("resetButton");
const cells = document.querySelectorAll(".cell");
const player = ["X", "O"];
let currentPlayer = 0;
let gameEnded = true;

const changePlayer = () => {
  //   if (currentPlayer === 0) {
  //     currentPlayer = 1;
  //   } else {
  //     currentPlayer = 0;
  //   }
  currentPlayer = currentPlayer === 0 ? 1 : 0;
  return player[currentPlayer];
};

const checkWinner = () => {};
const checkDraw = () => {};

cells.forEach((cell) => {
  cell.addEventListener("click", () => {
    console.log(player[currentPlayer]);
    if (!cell.textContent && !gameEnded) {
      cell.textContent = player[currentPlayer];
      if (checkWinner()) {
        gameEnded = true;
        alert(`O jogador ${player[currentPlayer]} venceu!`);
      } else if (checkDraw()) {
        gameEnded = true;
        alert("Empate!");
      } else {
        changePlayer();
      }
    }
  });
});

resetButton.addEventListener("click", () => {
  cells.forEach((cell) => {
    cell.textContent = "";
  });
  gameEnded = false;
  currentPlayer = 0;
  console.clear();
});
