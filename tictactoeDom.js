// tictactoeDom.js

document.addEventListener("DOMContentLoaded", function () {
    // Select the restart button
    var restart = document.querySelector("#b");

    // Select all the squares
    var squares = document.querySelectorAll("td");

    // Clear all the squares
    function clearBoard() {
        for (var i = 0; i < squares.length; i++) {
            squares[i].textContent = '';
        }
    }

    // Add a click event listener to the restart button
    restart.addEventListener('click', clearBoard);

    // Select cellOne
//    var cellOne = document.querySelector("#one");
//
//    // Add a click event listener to cellOne
//    cellOne.addEventListener('click', function () {
//        if (cellOne.textContent === '') {
//            cellOne.textContent = 'X';
//        } else if (cellOne.textContent === 'X') {
//            cellOne.textContent = 'O';
//        } else {
//            cellOne.textContent = '';
//        }
//    });

       function changeMarker(){

            if(this.textContent === ''){

                this.textContent = 'X';

            }else if (this.textContent === 'X'){

                this.textContent = 'O';

            }else{

                this.textContent = '';
            }
       }

       for (var i = 0; i<squares.length; i++){

            squares[i].addEventListener('click',changeMarker)

       }
});
