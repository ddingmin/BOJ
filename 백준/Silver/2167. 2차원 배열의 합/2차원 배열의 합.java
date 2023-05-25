import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();
    //static int[][] dp = new int[1000001];
    static int[] arr;
    static int[][] map;

    static int n, m;
    static ArrayList<int[]> list = new ArrayList<>();
    static Deque<Integer> queue = new ArrayDeque<>();

    public static void main(String[] args) throws Exception {
        input();
        solve();
        print();
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            int[] temp = new int[4];
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                temp[j] = Integer.parseInt(st.nextToken());
            }
            list.add(temp);
        }
    }

    private static void solve() {
        for (int[] temp : list) {
            int sum = 0;
            for (int i = temp[0] - 1; i < temp[2]; i++) {
                for (int j = temp[1] - 1; j < temp[3]; j++) {
                    sum += map[i][j];
                }
            }
            answer.append(sum + "\n");
        }
    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}