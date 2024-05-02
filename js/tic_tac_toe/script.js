"use strict";

const player = ["X", "O"];
let currentPlayer = 0;
const changePlayer = function () {
  if (currentPlayer === 0) {
    currentPlayer = 1;
  } else {
    currentPlayer = 0;
  }
  //   currentPlayer = currentPlayer === 0 ? 1 : 0;
  return player[currentPlayer];
};

const cell = document.querySelectorAll(".cell");
cell.forEach((cll) => {
  console.log(cll);
});
// console.log(cell);
