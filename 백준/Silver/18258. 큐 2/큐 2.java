import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();

    static int[] arr;
    static int n;
    static ArrayList<String> words = new ArrayList<>();
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
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String token = st.nextToken();
            if (token.equals("push")) {
                queue.add(Integer.parseInt(st.nextToken()));
            }
            else if (token.equals("pop")) {
                if (queue.size() > 0){
                    answer.append(queue.remove() + "\n");
                }
                else{
                    answer.append(-1 + "\n");
                }
            }
            else if (token.equals("size")) {
                answer.append(queue.size() + "\n");
            }
            else if (token.equals("empty")) {
                if (queue.size() > 0) {
                    answer.append(0 + "\n");
                }
                else {
                    answer.append(1 + "\n");
                }
            }
            else if (token.equals("front")) {
                if (queue.size() > 0) {
                    answer.append(queue.getFirst() + "\n");
                }
                else {
                    answer.append(-1 + "\n");
                }
            }
            else if (token.equals("back")) {
                if (queue.size() > 0) {
                    answer.append(queue.getLast() + "\n");
                }
                else {
                    answer.append(-1 + "\n");
                }
            }
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