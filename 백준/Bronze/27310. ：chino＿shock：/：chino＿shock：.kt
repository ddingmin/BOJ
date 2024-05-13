import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val emoji = readLine()

    sout.appendLine(solve(emoji))
    sout.flush()
}

fun solve(emoji: String): String {
    return (emoji.length + emoji.split("").count { it == ":" } + emoji.split("").count { it == "_" } * 5).toString()
}
