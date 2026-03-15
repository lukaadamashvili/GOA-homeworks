let number = Number(prompt("შემოიტანეთ რიცხვი:"));

let message = (number % 2 === 0) ? "Number is even" : "Number is odd";

console.log(message);



let age = Number(prompt("შემოიტანეთ თქვენი ასაკი:"));
let is_student = confirm("ხართ თუ არა სტუდენტი? (OK - კი, Cancel - არა)");

if (age >= 18 && age <= 24 && is_student) {
    console.log("შენ ხარ სტუდენტი და გეკუთვნის სტიპენდია");
} else if (age === 18 && !is_student) {
    console.log("18 წლის ხარ მარა სტუდენტი არა, რა სტიპენდიაზე ლაპარაკობ");
} else {
    console.log("ჯერ სკოლა დაამთავრე");
}



let car = prompt("შემოიტანეთ მანქანის მოდელი:");

switch (car.toLowerCase()) {
    case "bmw":
        console.log("გერმანული ხარისხი და სიმძლავრე.");
        break;
    case "mercedes":
        console.log("კომფორტი და ფუფუნება.");
        break;
    case "tesla":
        console.log("მომავლის ელექტრო მანქანა.");
        break;
    case "toyota":
        console.log("გამძლეობა და პრაქტიკულობა.");
        break;
    case "ferrari":
        console.log("სწრაფი და იტალიური სპორტული ავტომობილი.");
        break;
    default:
        console.log("ამ მოდელის შესახებ ინფორმაცია არ მაქვს.");
}





