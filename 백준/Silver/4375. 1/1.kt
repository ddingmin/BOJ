import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    readLines().forEach { sout.appendLine(solve(it.toInt())) }

    sout.flush()
}

fun solve(n: Int): String {
    var ans = 1
    var number = 0

    while (true) {
        number = number * 10 + 1
        number %= n
        if (number == 0) {
            break
        }
        ans++
    }
    return ans.toString()
}

