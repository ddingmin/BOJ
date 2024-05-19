import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val n = readLine().toInt()

    repeat(n) {
        val (count, word) = readLine().split(" ")
        sout.appendLine(solve(count.toInt(), word))
    }
    sout.flush()
}

fun solve(count: Int, word: String): String {
    return word.repeat(count)
}
