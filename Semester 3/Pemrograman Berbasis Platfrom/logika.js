const nilai = 90;
const sikap = 70;

const nilaiLulus = nilai >= 80;
const sikapLulus = sikap < 71;

const lulus = nilaiLulus && sikapLulus;
console.log(lulus);