function completeReservation() {

    // Getting values from HTML
    let reservedDate = document.getElementById("reservationDate").value;
    let inputReservedDate = new Date(reservedDate);
    let currentDate = new Date();
    let numberOfPeople = document.getElementById("numberOfPeople").value;

    // Variables for validation
    let dateValidation;
    let numberOfPeopleValidation;

    numberOfPeopleValidation = numberOfPeople >= 2; // if >=2, true, otherwise, false
    dateValidation = inputReservedDate > currentDate; // if reservation date > current date, true, otherwise, false

    // Presenting validation in HTML
    if (dateValidation == true && numberOfPeopleValidation == true) {
        document.getElementById("reservationResult").innerHTML = "Reservation confirmed successfully!";
    }

    if (dateValidation == true && numberOfPeopleValidation == false) {
        document.getElementById("reservationResult").innerHTML = "Your reservation must have at least 2 people!";
        document.getElementById("numberOfPeople").value = "";
    }

    if (dateValidation == false && numberOfPeopleValidation == true) {
        document.getElementById("reservationResult").innerHTML = "The date of your reservation cannot be earlier than today!";
        document.getElementById("reservationDate").value = "";
    }

}
