import java.io.BufferedWriter
import java.io.OutputStreamWriter
import kotlin.math.min

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val (n, w, h, l) = readLine()
        .split(" ").map { it.toInt() }

    sout.appendLine(solve(n, w, h, l))
    sout.flush()
}

fun solve(a: Int, b: Int, c: Int, d: Int): String {
    return min(a, (b / d) * (c / d)).toString()
}
