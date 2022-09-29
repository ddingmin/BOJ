import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();
    static int ans = 0;
    public static void main(String[] args) throws Exception {
        input();
        solve();
        print();
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a, b, c;
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        if (a == b && b == c){
            ans = 10000 + a * 1000;
        }
        else if (a == b || b == c || a == c) {
            ans = 1000;
            if (a == b){
                ans += a * 100;
            }
            else if (b == c){
                ans += b * 100;
            }
            else if (a == c){
                ans += a * 100;
            }
        }
        else{
            ans = Math.max(Math.max(a, b), c) * 100;
        }
    }

    private static void solve() {
        answer.append(ans);
    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}
