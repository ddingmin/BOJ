import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();
    static int[] dp;
    static int[] arr;
    static long temp = 0;

    static int n, m;
    static int a, b, c;
    static ArrayList<String> list = new ArrayList<>();
    static Deque<Pair> queue = new ArrayDeque<>();
    static HashSet<Integer> answers = new HashSet<>();
    static int[][][] visit;


    public static class Pair {
        int x, y, z;

        public Pair(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }
        public List<Pair> getPull() {
            List<Pair> pairList = new ArrayList<>();
            int minus;
            minus = Math.min(this.x, b - this.y);
            pairList.add(new Pair(this.x - minus, this.y + minus, this.z));
            minus = Math.min(this.z, b - this.y);
            pairList.add(new Pair(this.x, this.y + minus, this.z - minus));
            minus = Math.min(this.y, a - this.x);
            pairList.add(new Pair(this.x + minus, this.y - minus, this.z));
            minus = Math.min(this.z, a - this.x);
            pairList.add(new Pair(this.x + minus, this.y, this.z - minus));
            minus = Math.min(this.x, c - this.z);
            pairList.add(new Pair(this.x - minus, this.y, this.z + minus));
            minus = Math.min(this.y, c - this.z);
            pairList.add(new Pair(this.x, this.y - minus, this.z + minus));
            return pairList;
        }

        public boolean isVisited(){
            return visit[this.x][this.y][this.z] == 1;
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
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
    }

    private static void solve() {
        visit = new int[a + 1][b + 1][c + 1];
        visit[0][0][c] = 1;
        answers.add(c);
        int i, j, k;
        queue.add(new Pair(0, 0, c));
        while (!queue.isEmpty()) {
            Pair cur = queue.poll();
            for (Pair next : cur.getPull()) {
                if (!next.isVisited()){
                    visit[next.x][next.y][next.z] = 1;
                    queue.add(next);
                    if (next.x == 0) {
                        answers.add(next.z);
                    }
                }
            }

        }
        ArrayList<Integer> al = new ArrayList<>(answers);
        Collections.sort(al);
        for (Integer ans: al) {
            answer.append(ans).append(" ");
        }
    }


    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}