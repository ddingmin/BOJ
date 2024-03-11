import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    var temp = 0
    var idx = 0
    for (i in 1..5) {
        var input = readLine().split(" ").map { it.toInt() }
        input.sum().let {
            if (it > temp) {
                temp = it
                idx = i
            }
        }
    }

    sout.appendLine("$idx $temp")
    sout.close()
}

fun solve(n: Int, names: List<List<String>>): String {
    return ""
}
