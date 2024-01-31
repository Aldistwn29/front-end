const orang = {};

// Menambahkan atau mengubah
orang["nama"] = "Aldi";
orang["alamat"] = "Pasir Brntik";
orang["umur"] = 20;

// mengahapus umur
delete orang["umur"];
console.table(orang)