import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val n = readLine().toInt()

    sout.appendLine(solve(n))
    sout.close()
}

fun solve(n: Int): String {
    if (n == 1) return "0"

    return when {
        (n % 2 == 0) -> ((n * n) / 2).toString()
        else -> (((n * n) / 2) + 1).toString()
    }
}
