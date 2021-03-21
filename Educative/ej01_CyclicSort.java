class CyclicSort {

  public static void sort(int[] nums) {
    int i = 0;
    while (i < nums.length) {
      int j = nums[i] - 1;
      if (nums[i] != nums[j]) swap(nums, i, j);
      else i++;
    }
  }

  private static void swap(int[] arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }

  public static void main(String[] args) {
    int[] arr = new int[] {3, 1, 5, 4, 2};
    CyclicSort.sort(arr);
    for (int num : arr) System.out.print(num + " ");
    System.out.println();

    arr = new int[] {2, 6, 4, 3, 1, 5};
    CyclicSort.sort(arr);
    for (int num : arr) System.out.print(num + " ");
    System.out.println();

    arr = new int[] {1, 5, 6, 4, 3, 2};
    CyclicSort.sort(arr);
    for (int num : arr) System.out.print(num + " ");
    System.out.println();
  }
}
