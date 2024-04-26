import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val inputs = readLine().split(" ")
    val a = inputs[0].toInt()
    val b = inputs[1].toInt()

    sout.appendLine(solve(a, b))
    sout.flush()
}

fun solve(a: Int, b: Int): String {
    return (a * (b - 1) + 1).toString()
}
