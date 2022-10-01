import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();
    static int N = 0;
    static Double max = 0.0;
    static ArrayList<Double> arr = new ArrayList<>();
    public static void main(String[] args) throws Exception {
        input();
        solve();
        print();
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr.add(Double.parseDouble(st.nextToken()));
            max = Math.max(arr.get(i), max);
        }
    }

    private static void solve() {
        Double temp = 0.0;
        for (int i = 0; i < N; i++) {
            temp += arr.get(i) / max * 100;
        }
        Double ans;
        ans = temp / arr.size();
        answer.append(ans);
    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}
