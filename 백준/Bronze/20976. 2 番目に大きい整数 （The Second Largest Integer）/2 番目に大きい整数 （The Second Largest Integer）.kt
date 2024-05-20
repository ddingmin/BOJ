import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    sout.appendLine(readLine().split(" ").map { it.toInt() }.sorted().get(1).toString())
    sout.flush()
}

fun solve(count: Int, word: String): String {
    return word.repeat(count)
}
