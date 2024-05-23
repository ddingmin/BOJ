import java.io.BufferedWriter
import java.io.OutputStreamWriter
import kotlin.math.abs

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val (x, l, r) = readLine().split(" ").map { it.toInt() }

    sout.write(solve(x, l, r))
    sout.flush()
}

fun solve(x: Int, l: Int, r: Int): String {
    var temp = 100_001
    var ans = 0
    (l until r + 1).forEach { i ->
        if (abs(x - i) < temp) {
            temp = abs(x - i)
            ans = i
        }
    }
    return ans.toString()
}
