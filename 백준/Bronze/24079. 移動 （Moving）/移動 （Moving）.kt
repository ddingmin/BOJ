import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val x = readLine().trim().toInt()
    val y = readLine().trim().toInt()
    val z = readLine().trim().toInt()

    sout.appendLine(solve(x, y, z))
    sout.flush()
}

fun solve(x: Int, y: Int, z: Int): String {
    return if (x + y <= z) "1" else "0"
}
