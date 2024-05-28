import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val (x, y, z) = readLine().split(" ").map { it.toInt() }

    sout.appendLine(solve(x, y, z))
    sout.flush()
}

fun solve(x: Int, y: Int, z: Int): String {
    if (x == y || y == z || z == x) {
        return "S"
    }
    if (x + y == z || x + z == y || y + z == x) {
        return "S"
    }
    return "N"
}
