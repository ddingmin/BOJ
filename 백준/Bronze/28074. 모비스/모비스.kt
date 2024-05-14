import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.stream.Collectors.toMap

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val word = readLine().uppercase()

    sout.appendLine(solve(word))
    sout.flush()
    sout.close()
}

fun solve(word: String): String {
    val mobis = "MOBIS".split("").stream()
        .map { Pair(it, 1) }
        .filter { it.first != "" }
        .collect(toMap({ it.first }, { it.second }))

    word.split("")
        .forEach { mobis[it] = mobis.getOrDefault(it, 0) - 1 }

    return if (mobis.values.stream().allMatch { it <= 0 }) "YES" else "NO"
}
