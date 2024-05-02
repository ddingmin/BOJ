import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val winCount = readLines().count() { it == "W" }

    sout.appendLine(solve(winCount))
    sout.flush()
}

fun solve(winCount: Int): String {
    if (winCount >= 5) return "1"
    if (winCount >= 3) return "2"
    if (winCount >= 1) return "3"
    return "-1"
}
