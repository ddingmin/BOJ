import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val (a, b, c, d) = readLines().map { it.toInt() }

    sout.appendLine(solve(a, b, c, d))
    sout.flush()
}

fun solve(a: Int, b: Int, c: Int, d: Int): String {
    if (a == b && b == c && c == d) return "Fish At Constant Depth"
    if (b in (a + 1)..<c && c < d) return "Fish Rising"
    if (b in (c + 1)..<a && c > d) return "Fish Diving"
    return "No Fish"
}
