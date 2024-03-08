import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val n = readLine().toInt()
    val chats = readLines()

    sout.appendLine(solve(n, chats))
    sout.close()
}

fun solve(n: Int, chats: List<String>): String {
    var ans = 0

    var mp = mutableMapOf<String, Int>()

    for (id in chats) {
        if (id == "ENTER") {
            mp.clear()
        }
        else {
            if (!mp.contains(id)) {
                ans += 1
                mp[id] = 1
            }
            else {
                continue
            }
        }
    }

    return ans.toString()
}
