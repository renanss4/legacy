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

const checkWinner = () => {
  const winConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8], // Linhas
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8], // Colunas
    [0, 4, 8],
    [2, 4, 6], // Diagonais
  ];

  for (const condition of winConditions) {
    const [a, b, c] = condition;
    if (
      cells[a].textContent !== "" &&
      cells[a].textContent === cells[b].textContent &&
      cells[a].textContent === cells[c].textContent
    ) {
      return cells[a].textContent;
    }
  }
  return null;
};

const checkDraw = () => {
  for (const cell of cells) {
    if (cell.textContent === "") {
      return false;
    }
  }
  return true;
};

cells.forEach((cell) => {
  cell.addEventListener("click", () => {
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
  resetButton.textContent = "Reiniciar Jogo";
  cells.forEach((cell) => {
    cell.textContent = "";
  });
  gameEnded = false;
  currentPlayer = 0;
});
