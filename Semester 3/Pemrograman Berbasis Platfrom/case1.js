let nilai = "F";

switch(nilai){
    case "A":
        ucapan = "Wow anda lulus, Hebat!"
    case"B":
        ucapan = "Selamat anda lulus.";
        break;
    case"C":
        ucapan = "Anda lulus";
        break;
    case"D":
        ucapan = "Anda tidak lulus.";
        break;
    default:
        ucapan = "Mungkin anda salah Jurusan!"
        break;
}
console.log(ucapan);