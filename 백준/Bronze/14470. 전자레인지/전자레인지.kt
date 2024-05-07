import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val (a, b, c, d, e) = readLines().map { it.toInt() }

    sout.appendLine(solve(a, b, c, d, e))
    sout.flush()
}

fun solve(a: Int, b: Int, c: Int, d: Int, e: Int): String {
    if (a < 0) {
        return (-a * c + d + b * e).toString()
    }
    return ((b - a) * e).toString()
}
