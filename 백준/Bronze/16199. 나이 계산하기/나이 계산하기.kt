import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() = with(System.`in`.bufferedReader()) {
    val sout = BufferedWriter(OutputStreamWriter(System.out))

    val birthDate = readLine().split(" ")

    val today = readLine().split(" ")

    sout.appendLine(solve(birthDate, today))
    sout.close()
}

fun solve(birthDate: List<String>, today: List<String>): String {
    var ans = ""

    val bYear = birthDate[0].toInt()
    val bMonth = birthDate[1].toInt()
    val bDay = birthDate[2].toInt()


    val tYear = today[0].toInt()
    val tMonth = today[1].toInt()
    val tDay = today[2].toInt()

    if (bMonth < tMonth || (bMonth == tMonth && bDay <= tDay)) {
        ans = ans + (tYear - bYear).toString() + "\n"
    } else {
        ans = ans + (tYear - bYear - 1).toString() + "\n"
    }

    ans = ans + (tYear - bYear + 1).toString() + "\n"
    ans = ans + (tYear - bYear).toString() + "\n"

    return ans
}
