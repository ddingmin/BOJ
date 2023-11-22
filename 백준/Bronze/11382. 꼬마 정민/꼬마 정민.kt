fun main() = with(System.`in`.bufferedReader()) {
    var nums = readLine().split(" ").map { it.toLong() }
    print(nums.sum())
}
