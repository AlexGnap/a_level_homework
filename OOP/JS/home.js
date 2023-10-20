//1
for (let i = 1; i <= 10; i++) {
    if (i % 3 === 0) {
        console.log("FizBuz");
    } else if (i % 2 === 0) {
        console.log("Fiz");
    } else {
        console.log("Buz");
    }
}



//2
function factorial(numb) {
    let result = 1;
    for (let i = 2; i <= numb; i++) {
        result *= i;
    }
    return result;
}



//3
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



//4
function floorAndPorch(apartmentNumber) {

    let porch = apartmentNumber / 27;
    porch = porch - porch % 1;

    let apartmentInPorch = apartmentNumber % 27;

    let floor = apartmentInPorch / 3;
    floor = floor - floor % 1;

    console.log(`My appartment №${apartmentNumber} is in ${porch} porch at ${floor}th floor`);
}

floorAndPorch(39);