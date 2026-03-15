// 1)
let age = prompt("შეიყვანე შენი ასაკი");

let result = age >= 18 ? "სრულწლოვანი ხარ" : "არ ხარ სრულწლოვანი";

alert(result)

// 2)
let num = prompt("შეიყვანე რიცხვი 1-დან 5-ის ჩათვლით:");

switch (num) {
    case "1":
     alert("რიცხვი არის 1");
     break;
    case "2":
     alert("რიცხვი არის 2");
     break;
    case "3":
     alert("რიცხვი არის 3");
     break;
    case "4":
     alert("რიცხვი არის 5");
     break;
    case "5":
     alert("რიცხვი არის 5");
     break;
    default:
     alert("არასწორი რიცხვია")
}

// 3)
let age2 = prompt("შეიყვანე შენი ასაკი");

if (age2 >= 18 && age2 <= 60) {
    alert("მუშაობა შეგიძლია");
}   else if (age2 > 60) {
    alert("გადი პენსიაზე რა თავს იკლავ")
}   else {
    alert("არაა სამუშაო ასაკი")
}

// 4)
let color = prompt("შეიყვანე ფერი (red,blue,green):")

switch (color) {
    case "red":
        alert("წითელი");
        break;
    case "blue":
        alert("ლურჯი");
        break;
    case "green":
        alert("მწვანე");
        break;
    default:
        alert("ფერი ვერ მოიძებნა")
}