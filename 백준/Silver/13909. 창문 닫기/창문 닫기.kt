import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val n = readLine().toInt()

    sout.appendLine(solve(n))
    sout.close()
}

fun solve(n: Int): String {
    var ans = 0

    var i = 1
    while (i * i <= n) {
        i += 1
        ans += 1
    }

    return ans.toString()
}
