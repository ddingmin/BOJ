import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.lang.Integer.sum

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val a = readLine()
    val b = readLine()
    val c = readLine()
    sout.appendLine(solve(a, b, c))

    sout.flush()
}

fun solve(a: String, b: String, c: String): String {
    var ans = ""

    ans += (sum(a.toInt(), b.toInt()) - c.toInt()).toString()
    ans += "\n"
    ans += (a + b).toInt() - c.toInt()

    return ans
}

