import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val t = readLine().toInt()

    repeat(t) {
        val n = readLine().toInt()
        repeat(n) {
            val (a, b) = readLine().split(" ").map { it.toLong() }
            sout.appendLine(solve(a.toLong(), b.toLong()))
        }
    }
    sout.flush()
}

fun solve(a: Long, b: Long): String {
    return (a + b).toString() + " " + (a * b).toString()
}
