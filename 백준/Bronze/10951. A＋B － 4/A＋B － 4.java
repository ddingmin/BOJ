import java.io.*;
import java.util.*;

class Main {

    static int N;
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
        String input = "";
        int a, b;
        while ((input = br.readLine()) != null){
            st = new StringTokenizer(input);
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            answer.append(a + b + "\n");
        }

    }

    private static void solve() {

    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}
