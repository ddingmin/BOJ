import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val (n, x) = readLine().split(" ").map { it.toLong() }
    val arr = readLine().split(" ").map { it.toInt() }

    sout.appendLine(solve(n, x, arr))
    sout.flush()
}

fun solve(n: Long, x: Long, arr: List<Int>): String {
    return ((1 until n).map { i ->
        arr[i.toInt()] + arr[i.toInt() - 1]
    }.min().toLong() * x).toString()
}
