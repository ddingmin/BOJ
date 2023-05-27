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
//        StringTokenizer st new StringTokenizer(br.readLine());
        N = Integer.parseInt(br.readLine());
    }

    private static void solve() {
        long k = 0;
        long len = 3;

        while (len < N) {
            k += 1;
            len = len * 2 + (k + 3);
        }

        answer.append(moo(k + 3, len, N));

    }

    private static char moo(long k, long len, long cur) {
        long prevLength = (len - k) / 2;
        // 이전 스탭 길이보다 작은경우
        if (cur <= prevLength) {
            return moo(k - 1, prevLength, cur);
        }
        // 이전 스탭 + moo..o보다 큰 경우
        else if (cur > prevLength + k) {
            return moo(k - 1, prevLength, cur - (prevLength + k));
        }
        // 이전스탭 + 1의 경우
        else if (prevLength + 1 == cur) {
            return 'm';
        }
        return 'o';
    }


    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}