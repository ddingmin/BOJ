import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val numbers = readLines().map { it.toInt() }

    numbers
        .filter { it > 0 }
        .forEach {
            sout.append(solve(it))
        }
    sout.flush()
    sout.close()
}

fun solve(number: Int): String {
    var answer = ""
    (1..number).forEach {
        answer += "${"*".repeat(it)}\n"
    }
    return answer
}
