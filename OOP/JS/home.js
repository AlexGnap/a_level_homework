for (let i = 1; i <= 10; i++) {
    if (i % 3 === 0) {
        console.log("FizBuz");
    } else if (i % 2 === 0) {
        console.log("Fiz");
    } else {
        console.log("Buz");
    }
}



function factorial(numb) {
    let result = 1;
    for (let i = 2; i <= numb; i++) {
        result *= i;
    }
    return result;
}



const sheetsInReamPaper = 500;
const consumptionPerWeek = 1200;
const weeksAmount = 8;

let overallConsump = consumptionPerWeek * weeksAmount;

let fullReamPaper = overallConsump / sheetsInReamPaper;
let notRoundedResult = overallConsump % sheetsInReamPaper;

let reamsNeeded;
if (notRoundedResult > 0) {
    reamsNeeded = fullReamPaper + 1;
} else {
    reamsNeeded = fullReamPaper;
}

reamsNeeded = reamsNeeded - (reamsNeeded % 1)

console.log(reamsNeeded)