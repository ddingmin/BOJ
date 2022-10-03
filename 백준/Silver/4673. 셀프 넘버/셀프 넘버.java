import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();

    static int[] arr = new int[10001];

    public static void main(String[] args) throws Exception {
        input();
        solve();
        print();
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //StringTokenizer st = new StringTokenizer(br.readLine());
    }

    private static void solve() {
        for (int i = 1; i < 10001; i++) {
            check(i);
            if (arr[i] == 0){
                answer.append(i + "\n");
            }
        }
    }

    public static void check(int a){
        int temp, c;
        if (arr[a] == 0){
            while (true){
                temp = a;
                c = a;
                while (temp > 0){
                    c += temp % 10;
                    temp /= 10;
                }
                if (c > 10000 || arr[c] == 1){
                    break;
                }
                else{
                    arr[c] = 1;
                    a = c;
                }
            }
        }
    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}
