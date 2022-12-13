std::vector<int> FindMaxSlidingWindow(std::vector<int> &nums, int windowSize)
{
    std::vector<int> result;
    std::deque<int> window;
    if (nums.size() == 0)
    {
        return result;
    }
    if (windowSize > nums.size())
    {
        windowSize = nums.size();
    }
    bool check = false;
    for (int i = 0; i < windowSize; ++i)
    {
        while (!window.empty() && nums[i] >= nums[window.back()])
        {
            check = true;
            window.pop_back();
        }
        check = false;
        window.push_back(i);
    }
    result.push_back(nums[window.front()]);
    for (int i = windowSize; i < nums.size(); ++i)
    {
        while (!window.empty() && nums[i] >= nums[window.back()])
        {
            check = true;
            window.pop_back();
        }
        check = false;
        if (!window.empty() && window.front() <= i - windowSize)
        {
            window.pop_front();
        }
        window.push_back(i);
        result.push_back(nums[window.front()]);
    }
    return result;
}

// Driver code
int main()
{
    std::vector<int> targetList = {3, 3, 3, 3, 2, 4, 3, 2, 3, 18};
    std::vector<std::vector<int>> numsList = {{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
                 {10, 9, 8, 7, 6, 5, 4, 3, 2, 1},
                 {10, 10, 10, 10, 10, 10, 10, 10, 10, 10},
                 {1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30},
                 {10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67},
                 {4, 5, 6, 1, 2, 3},
                 {9, 5, 3, 1, 6, 3},
                 {2, 4, 6, 8, 10, 12, 14, 16},
                 {-1, -1, -2, -4, -6, -7},
                 {4, 4, 4, 4, 4, 4}};

    for (int i = 0; i < targetList.size(); i++)
    {
        std::cout << i + 1 << ".\tOriginal array:\t" << Print(numsList[i]) << std::endl;
        std::cout << "\tWindow size:\t" << std::to_string(targetList[i]) << std::endl;
        std::vector<int> result = FindMaxSlidingWindow(numsList[i], targetList[i]);
        std::cout << "\n\tMax:\t" << Print(result) << std::endl;
        std::cout << std::string(100, '-') << std::endl;
    }
}
