const dataDiri={
    nama : "Aldi Setiawan",
    nim : 20220040054,
    kelas : "TI22H",
};

const nilai={
    rpl : 90,
    imk : 100,
    pbp : 90,
    mn : 90,
    jrkom : 90,
};

console.log("Nama:",dataDiri.nama);
console.log("nim:",dataDiri.nim);
console.log("kelas:",dataDiri.kelas);
console.log("\nNilai");
console.log("Rekayasa Perangkat Lunak:",nilai.rpl);
console.log("Interaksi Manusia dan Komputer:",nilai.imk);
console.log("Pemrograman Berbasis Platfrom:",nilai.pbp);
console.log("Metode Numerik:",nilai.mn);
console.log("Jaringan Komputer:",nilai.jrkom);

const rataRata = (nilai.rpl + nilai.imk) / 2;
console.log("Rata-Rata:",rataRata);