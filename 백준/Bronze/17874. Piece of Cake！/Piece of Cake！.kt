import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val (n, h, v) = readLine().split(" ").map { it.toInt() }
    
    sout.appendLine(solve(n, h, v))
    sout.flush()
}

fun solve(n: Int, h: Int, v: Int): String {
    val maxH = if (h > n - h) h else n - h
    val maxV = if (v > n - v) v else n - v
    return (maxH * maxV * 4).toString()
}
