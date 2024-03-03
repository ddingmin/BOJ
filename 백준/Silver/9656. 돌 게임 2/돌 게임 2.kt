import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    var n = readLine().toInt()

    sout.appendLine(solve(n))
    sout.close()
}

fun solve(n: Int): String {
    if (n % 2 == 0){
        return "SK"
    }
    return "CY"
}
