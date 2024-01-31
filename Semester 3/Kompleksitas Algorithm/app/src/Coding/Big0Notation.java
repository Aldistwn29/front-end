package Coding;

public class Big0Notation{
    int programmingScore [] = {100, 90, 60, 85, 70, 100, 80};

    int getProgrammingScore(int index){
        if(index >=0 && index < programmingScore.length)
            return programmingScore[index];
        return 0;
        // Logic nya yaitu ketika index yg kita panggila lebih dari sama dengan 0 dan index lebih dari
        // Panjang variabel Array(ProgrammingScore) maka akan mengembalikan dengan nilai 0
        // atau outputnya 0

    }
    public static void main(String[] args){
        Big0Notation c = new Big0Notation();
        System.out.println(c.getProgrammingScore(20));
    }
}