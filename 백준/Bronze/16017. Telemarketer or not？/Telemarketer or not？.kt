import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val (a, b, c, d) = readLines().map { it.toInt() }

    sout.appendLine(solve(a, b, c, d))
    sout.flush()
}

fun solve(a: Int, b: Int, c: Int, d: Int): String {
    return when {
        (a == 8 || a == 9) && (d == 8 || d == 9) && (b == c) -> {
            "ignore"
        }

        else -> "answer"
    }
}
