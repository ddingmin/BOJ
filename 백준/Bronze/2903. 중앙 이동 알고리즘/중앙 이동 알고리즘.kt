import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.lang.Math.pow

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val n = readLine().toInt()

    sout.appendLine(solve(n))
    sout.flush()
}

fun solve(n: Int): String {
    var start = 1

    repeat(n) {
        start *= 2
    }

    return pow(start + 1.toDouble(), 2.0).toInt().toString()
}

