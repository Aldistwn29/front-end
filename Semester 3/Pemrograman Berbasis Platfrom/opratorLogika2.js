const nilaiUjian = 76;
const nilaiAbsen = 70;

const lulusUjian = nilaiUjian > 75;
const lulusAbsen = nilaiAbsen > 75;

lulus = lulusUjian || lulusAbsen;
console.log(lulus)