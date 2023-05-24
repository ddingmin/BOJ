import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();

    static Integer[] arr;
    static int n;

    public static void main(String[] args) throws Exception {
        input();
        solve();
        print();
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        arr = new Integer[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
    }

    private static void solve() {
        Arrays.sort(arr, Collections.reverseOrder());
        int temp = 0;
        for (int i = 0; i < n; i++) {
            if (temp < arr[i] + i + 2){
                temp = arr[i] + i + 2;
            }
        }
        answer.append(temp + "\n");
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