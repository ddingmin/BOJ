import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val (numberOfAntenna, numberOfEyes) = readLines()
        .map { it.trim().toInt() }

    sout.appendLine(solve(numberOfAntenna, numberOfEyes))
    sout.flush()
}

fun solve(numberOfAntenna: Int, numberOfEyes: Int): String {
    var answers = ""
    if (numberOfAntenna >= 3 && numberOfEyes <= 4) {
        answers += "TroyMartian\n"
    }
    if (numberOfAntenna <= 6 && numberOfEyes >= 2) {
        answers += "VladSaturnian\n"
    }
    if (numberOfAntenna <= 2 && numberOfEyes <= 3) {
        answers += "GraemeMercurian\n"
    }
    return answers
}
