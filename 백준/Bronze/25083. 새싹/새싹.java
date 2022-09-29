import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();

    public static void main(String[] args) throws Exception {
        input();
        solve();
        print();
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());


    }

    private static void solve() {
        answer.append("         ,r'\"7\n");
        answer.append("r`-_   ,'  ,/\n");
        answer.append(" \\. \". L_r'\n");
        answer.append("   `~\\/\n");
        answer.append("      |\n");
        answer.append("      |\n");
        //answer.append(str);
    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}
