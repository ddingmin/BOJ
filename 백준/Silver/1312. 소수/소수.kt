import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    var input = readLine().split(" ").map { it.toInt() }
    val a = input[0]
    val b = input[1]
    val n = input[2]

    sout.appendLine(solve(a, b, n))
    sout.close()
}

fun solve(a: Int, b: Int, n: Int): String {
    var temp = a
    for (i in 1..n) {
        temp = temp % b * 10
    }
    return (temp / b).toString()
}
