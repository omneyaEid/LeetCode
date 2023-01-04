import java.util.HashMap;

class Solution {
    public int minimumRounds(int[] tasks) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int t : tasks) {
            map.put(t, map.getOrDefault(t, 0) + 1);
        }

        int count = 0;
        for (int key : map.keySet()) {
            int value = map.get(key);
            if (value == 1) {
                return -1;
            } else if (value == 2) {
                count += 1;
            } else if (value % 3 == 0) {
                count += value / 3;
            } else {
                count += value / 3 + 1;
            }
        }
        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        int[] array = {2, 2, 3, 3, 2, 4, 4, 4, 4, 4};
        System.out.println(s.minimumRounds(array));
    }
}