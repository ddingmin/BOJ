import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};

    static boolean[] dp;
    static int[][] map;
    static int[] nums;
    static boolean[][] visit;
    static long temp = 0;
    static int n;

    static int N;
    static ArrayList<Integer> answerList = new ArrayList<>();
    static Deque<Pair> queue = new ArrayDeque<>();
    static HashSet<Integer> answerSetList = new HashSet<>();


    public static class Pair {
        int x, y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        @Override
        public String toString() {
            return "Pair show: {x: " + this.x + ", y: " + this.y + "}";
        }
    }

    public static void main(String[] args) throws Exception {
        input();
        solve();
        print();
    }


    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
//        StringTokenizer st = new StringTokenizer(br.readLine());
    }

    private static void solve() {
        int ans = 1;
        for (int i = 1; i < n; i++) {
            if (Integer.toString(i).contains("50")) {
                ans += 2;
            }
            else {
                ans += 1;
            }
        }
        answer.append(ans).append("\n");
    }


    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}