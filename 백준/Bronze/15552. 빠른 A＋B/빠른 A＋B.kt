import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    var sout = BufferedWriter(OutputStreamWriter(System.out))

    val n = readLine().toInt()
    for (i in 1..n) {
        val nums = readLine().split(" ").map { it.toInt() }
        sout.appendLine(nums.sum().toString())
    }
    sout.flush()
}
