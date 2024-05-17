import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val (l, r) = readLine().split(" ").map { it.toInt() }

    sout.appendLine(solve(l, r))
    sout.flush()
    sout.close()
}

fun solve(l: Int, r: Int): String {
    // return Odd, Even, Not a moose
    return if (l == r) {
        if (l == 0) "Not a moose"
        else "Even ${l + r}"
    } else {
        "Odd ${2 * maxOf(l, r)}"
    }
}
