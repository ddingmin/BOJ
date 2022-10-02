import java.io.*;
import java.util.*;

class Main {
    static StringBuffer answer = new StringBuffer();
    static int N = 0;
    static Double max = 0.0;
    static ArrayList<List> arr = new ArrayList<>();
    public static void main(String[] args) throws Exception {
        input();
        solve();
        print();
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int C = Integer.parseInt(st.nextToken());
            Double sum = 0.0;
            ArrayList<Double> temp = new ArrayList<>();
            for (int j = 0; j < C; j++) {
                temp.add(Double.parseDouble(st.nextToken()));
                sum += temp.get(j);
            }
            temp.add(sum / C);
            arr.add(temp);
        }
    }

    private static void solve() {
        for (int i = 0; i < N; i++) {
            int last, overMean;
            Double mean;
            last = arr.get(i).size() - 1;
            mean = (Double) arr.get(i).get(last);
            overMean = 0;
            for (int j = 0; j < last; j++) {
                //answer.append(arr.get(i).get(j) + " ");
                if ((Double) arr.get(i).get(j) > mean){
                    overMean += 1;
                }
            }
            Double ans = (double) overMean / (double) last * 100.0;
            answer.append(String.format("%.3f", ans) + "%\n");
            //answer.append(ans + "\n");

        }

    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer.toString());
        bw.flush();
    }
}
