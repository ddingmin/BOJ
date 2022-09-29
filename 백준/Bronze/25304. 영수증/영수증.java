import java.io.*;
import java.util.*;

class Main {

    static int X, N, ans;
    static int[][] price = new int[100][2];
    static StringBuffer answer = new StringBuffer();

    public static void main(String[] args) throws Exception {
        input();
        solve();
        print();
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        // br.readLine(); 한줄 입력받기
        // st = new StringTokenizer(br.readLine()); 한줄 입력받고, 쪼갤 준비
        // st.nextToken(); 토큰 단위로 하나씩 쪼개기
        X = Integer.parseInt(br.readLine());
        N = Integer.parseInt(br.readLine());
        int a, b;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            price[i][0] = a;
            price[i][1] = b;
        }
    }

    private static void solve() {
        int temp = 0;
        for (int i = 0; i < N; i++) {
            temp += price[i][0] * price[i][1];
        }
        if (temp == X){
            answer.append("Yes");
        }
        else{
            answer.append("No");
        }
    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}
