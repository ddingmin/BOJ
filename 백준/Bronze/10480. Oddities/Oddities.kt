import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val n = readLine().toInt()
    repeat(n) {
        val t = readLine().toInt()
        sout.appendLine(solve(t))
    }

    sout.flush()
}

fun solve(t: Int): String {
    return if (t % 2 == 0) "$t is even" else "$t is odd"
}
