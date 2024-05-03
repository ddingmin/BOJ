import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val (ca, ba, pa) = readLine().split(" ").map { it.toInt() }
    val (cr, br, pr) = readLine().split(" ").map { it.toInt() }

    sout.appendLine(solve(ca, ba, pa, cr, br, pr))
    sout.flush()
}

fun solve(ca: Int, ba: Int, pa: Int, cr: Int, br: Int, pr: Int): String {
    val c = maxOf(0, cr - ca)
    val b = maxOf(0, br - ba)
    val p = maxOf(0, pr - pa)
    return "${c + b + p}"
}
