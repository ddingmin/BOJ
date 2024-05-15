import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val (k, w, m) = readLine().split(" ").map { it.toLong() }

    sout.appendLine(solve(k, w, m))
    sout.flush()
    sout.close()
}

fun solve(k: Long, w: Long, m: Long): String {
    val need = w - k
    if (need <= 0) return "0"

    return (need / m).let { if (need % m == 0L) it else it + 1 }.toString()
}
