import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val (speed, limit) = readLines().map { it.toInt() }

    sout.appendLine(solve(limit, speed))
    sout.flush()
    sout.close()
}

fun solve(speed: Int, limit: Int): String {
    return when {
        speed <= limit -> "Congratulations, you are within the speed limit!"
        speed <= limit + 20 -> "You are speeding and your fine is $100."
        speed <= limit + 30 -> "You are speeding and your fine is $270."
        else -> "You are speeding and your fine is $500."
    }
}
