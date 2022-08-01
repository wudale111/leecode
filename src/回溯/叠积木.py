class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        if (k == 1) return true; // 特判
        Arrays.sort(nums);;
        int n = nums.length;
        int target = 0;
        int max = 0;
        for (int i : nums) target += i;
        if (target % k != 0) return false; // 特判
        target /= k;
        if (target < nums[n - 1]) return false; // 特判
        int[] sums = new int[k];
        return dfs(nums, n - 1, 0, sums, k, target);
    }
    private boolean dfs(int[] nums, int cur, int used, int[] sums, int k, int target) {
        if (cur < 0) {
           return true;
        }
        if (used < k) {
            sums[used] = nums[cur];
            if (dfs(nums, cur - 1, used + 1, sums, k, target)) return true;
            sums[used] = 0;
        }
        for (int i = 0; i < used; i++) {
            // 如果当前桶和上一个桶内的元素和相等，则跳过
            // 原因：如果元素和相等，那么 nums[cur] 选择上一个桶和选择当前桶可以得到的结果是一致的
            if (i > 0 && sums[i] == sums[i - 1]) continue;
            if (sums[i] + nums[cur] <= target) {
                sums[i] += nums[cur];
                if (dfs(nums, cur - 1, used, sums, k, target)) return true;
                sums[i] -= nums[cur];
            }
        }
        return false;
    }
}




import java.util.*;

public class dieJiMu {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String[] s = in.nextLine().split(" ");
        int[] nums = new int[s.length];
        for (int i = 0; i < nums.length; i++) {
            nums[i] = Integer.parseInt(s[i]);
        }
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        Arrays.sort(nums);

        int res = -1;
        for (int i = 2; i <= sum / 2; i++) {
            if (sum % i != 0) continue;
            int score = sum / i;
            if(nums[nums.length - 1] > score){
                continue;
            }
            //建立一个长度为k的桶
            int[] arr = new int[i];
            //桶的每一个值都是子集的和
            Arrays.fill(arr, score);
            if (dfs (nums, nums.length - 1, 0, arr, i, score)) {
                res = Math.max(res, i);
            }
        }
        System.out.println(res);
    }
    public static boolean dfs(int[] nums, int cur, int used, int[] arr, int k, int score){
        //已经遍历到了-1说明前面的所有数都正好可以放入桶里，那所有桶的值此时都为0，说明找到了结果，返回true
        if(cur < 0){
            return true;
        }
        if (used < k) {
            arr[used] = nums[cur];
            if (dfs(nums, cur - 1, used + 1, arr, k, score)) {
                return true;
            }
            arr[used] = 0;
        }
        //遍历k个桶
        for(int i = 0; i < used; i++){
            // 如果当前桶和上一个桶内的元素和相等，则跳过
            // 原因：如果元素和相等，那么 nums[cur] 选择上一个桶和选择当前桶可以得到的结果是一致的
            if (i > 0 && arr[i] == arr[i - 1]) continue;
            if (arr[i] + nums[cur] <= score) {
                arr[i] += nums[cur];
                if (dfs(nums, cur - 1, used, arr, k, score)) return true;
                arr[i] -= nums[cur];
            }
        }
        return false;
    }
}
