package cd_letters_to_nums;

class Main{
    public static void main(String[] args) {
        lettersToNums("abc, d, eeeeee");
    }

    static int lettersToNums(String x){
        int counter = 0;
        String[] strings = x.split("");
        for (String i: strings){
            if ("ABCDEFGHIJKLMNOPQRSTUVXYZ".contains(i.toUpperCase())){
                char c = i.charAt(0);
                counter += (int) c - 96;
            }
        }
        return counter;
    }
}