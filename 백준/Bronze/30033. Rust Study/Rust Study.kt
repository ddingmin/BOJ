import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val n = readLine().toInt()
    val arr = readLine().split(" ").map { it.toInt() }
    val realArr = readLine().split(" ").map { it.toInt() }

    sout.write(solve(n, arr, realArr))
    sout.flush()
}

fun solve(n: Int, arr: List<Int>, real: List<Int>): String {
    var ans = 0
    
    (0..n - 1).forEach {
        if (arr[it] <= real[it]) ans += 1
    }

    return ans.toString()
}
