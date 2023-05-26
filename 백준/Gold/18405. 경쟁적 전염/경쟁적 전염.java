import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};
    static Deque<Pair>[] virusQueue;

    static int[] dp;
    static int[][] map;
    static int[][] visit;
    static long temp = 0;

    static int n, m, k, second, ansX, ansY;
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
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        map = new int[n][n];
        visit = new int[n][n];
        virusQueue = new Deque[k + 1];
        for (int i = 0; i < k + 1; i++) virusQueue[i] = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(s[j]);
                if (map[i][j] > 0) {
                    virusQueue[map[i][j]].add(new Pair(i, j));
                }

            }
        }
        st = new StringTokenizer(br.readLine());
        second = Integer.parseInt(st.nextToken());
        ansX = Integer.parseInt(st.nextToken()) - 1;
        ansY = Integer.parseInt(st.nextToken()) - 1;
    }

    private static void solve() {
        for (int sec = 0; sec < second; sec++) {
            for (int virusIndex = 1; virusIndex < k + 1; virusIndex++) {
                int maxSize = virusQueue[virusIndex].size();
                for (int v = 0; v < maxSize; v++) {
                    Pair cur = virusQueue[virusIndex].poll();
                    for (int kk = 0; kk < 4; kk++) {
                        int x = cur.getX() + dx[kk];
                        int y = cur.getY() + dy[kk];

                        if (0 <= x && x < n && 0 <= y && y < n){
                            if(map[x][y] == 0) {
                                map[x][y] = map[cur.x][cur.y];
                                virusQueue[virusIndex].add(new Pair(x, y));
                            }
                        }
                    }
                }
            }
        }
        answer.append(map[ansX][ansY]).append("\n");
        //for (int i = 0; i < n; i++) answer.append(Arrays.toString(map[i])).append("\n");
    }


    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}