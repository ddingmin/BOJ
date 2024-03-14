import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    var word = readLine().toString()

    sout.appendLine(solve(word))
    sout.close()
}

fun solve(word: String): String {
    return word.count { it in "aeiou" }.toString()
}
