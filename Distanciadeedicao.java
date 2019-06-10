package javaapplication1;

// BERNARDO BORDIN, MAX E VICTOR SCHERER

public class Distanciadeedicao {

    public static int ed(String S, String T, int i, int j) {
        if (i == 0 && j == 0) {
            return 0;
        }
        if (i == 0 && j != 0) {
            return j;
        }
        if (j == 0 && i != 0) {
            return i;
        }

        if (S.charAt(i) == T.charAt(j)) {
            return ed(S, T, i - 1, j - 1);
        } else {
            int subs = ed(S, T, i - 1, j - 1) + 1;
            int ins = ed(S, T, i, j - 1) + 1;
            int rem = ed(S, T, i - 1, j) + 1;

            if (subs < ins && subs < rem) {
                return subs;
            }
            if (ins < subs && ins < rem) {
                return ins;
            }
            return rem;
        }
    }

    public static void main(String[] args) {
        String S = "abcdadja";
        String T = "aaaaaaaa";
        int i = S.length()-1;
        int j = T.length()-1;
        ed(S, T, i, j);
        System.out.println(ed(S, T, i, j));

    }

}
