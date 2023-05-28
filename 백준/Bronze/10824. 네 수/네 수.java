import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};

    static boolean[] dp;
    static int[][] map;
    static boolean[][] visit;
    static long temp = 0;
    static long a, b, c, d;

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
        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Long.parseLong(st.nextToken());
        b = Long.parseLong(st.nextToken());
        c = Long.parseLong(st.nextToken());
        d = Long.parseLong(st.nextToken());

    }

    private static void solve() {
        long num1, num2;
        num1 = Long.parseLong(Long.toString(a) + Long.toString(b));
        num2 = Long.parseLong(Long.toString(c) + Long.toString(d));
        answer.append(num1 + num2).append("\n");
    }


    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}